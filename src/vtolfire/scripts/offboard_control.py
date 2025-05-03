#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool, CommandBoolRequest, SetMode, SetModeRequest
from std_msgs.msg import Bool

current_state = State()
override_active = False

def state_cb(msg):
    global current_state
    current_state = msg

def override_cb(msg):
    global override_active
    override_active = msg.data

if __name__ == "__main__":
    rospy.init_node("offboard_control_node")

    state_sub = rospy.Subscriber("mavros/state", State, callback=state_cb)
    override_sub = rospy.Subscriber("/fire_detection/override_active", Bool, callback=override_cb)
    local_pos_pub = rospy.Publisher("mavros/setpoint_position/local", PoseStamped, queue_size=10)

    rospy.wait_for_service("/mavros/cmd/arming")
    arming_client = rospy.ServiceProxy("/mavros/cmd/arming", CommandBool)

    rospy.wait_for_service("/mavros/set_mode")
    set_mode_client = rospy.ServiceProxy("/mavros/set_mode", SetMode)

    rate = rospy.Rate(20)

    while not rospy.is_shutdown() and not current_state.connected:
        rospy.loginfo_throttle(5, "Waiting for FCU connection...")
        rate.sleep()

    pose = PoseStamped()
    pose.pose.position.x = 2
    pose.pose.position.y = 2
    pose.pose.position.z = 2

    for _ in range(100):
        local_pos_pub.publish(pose)
        rate.sleep()

    offb_set_mode = SetModeRequest(custom_mode='OFFBOARD')
    arm_cmd = CommandBoolRequest(value=True)
    last_req = rospy.Time.now()

    while not rospy.is_shutdown():
        now = rospy.Time.now()

        if current_state.mode != "OFFBOARD" and current_state.mode != "AUTO.RTL" and (now - last_req > rospy.Duration(5.0)):
            if set_mode_client.call(offb_set_mode).mode_sent:
                rospy.loginfo("OFFBOARD enabled")
            last_req = now

        elif not current_state.armed and current_state.mode != "AUTO.RTL" and (now - last_req > rospy.Duration(5.0)):
            if arming_client.call(arm_cmd).success:
                rospy.loginfo("Vehicle armed")
            last_req = now

        if current_state.mode == "OFFBOARD" and not override_active:
            local_pos_pub.publish(pose)

        rate.sleep()
