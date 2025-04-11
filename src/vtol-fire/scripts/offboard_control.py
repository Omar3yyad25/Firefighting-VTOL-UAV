#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool, CommandBoolRequest, SetMode, SetModeRequest

current_state = State()

def state_cb(msg):
    global current_state
    current_state = msg

if __name__ == "__main__":
    rospy.init_node("offboard_control_node")

    state_sub = rospy.Subscriber("mavros/state", State, callback=state_cb)
    local_pos_pub = rospy.Publisher("mavros/setpoint_position/local", PoseStamped, queue_size=10)

    rospy.wait_for_service("/mavros/cmd/arming")
    arming_client = rospy.ServiceProxy("/mavros/cmd/arming", CommandBool)

    rospy.wait_for_service("/mavros/set_mode")
    set_mode_client = rospy.ServiceProxy("/mavros/set_mode", SetMode)

    rate = rospy.Rate(20)

    # Wait for connection
    while not rospy.is_shutdown() and not current_state.connected:
        rospy.loginfo_throttle(5, "Waiting for FCU connection...")
        rate.sleep()

    # Target position
    pose = PoseStamped()
    pose.pose.position.x = 2
    pose.pose.position.y = 2
    pose.pose.position.z = 2

    # Send 100 initial setpoints before switching to OFFBOARD
    for _ in range(100):
        local_pos_pub.publish(pose)
        rate.sleep()

    # Prepare requests
    offb_set_mode = SetModeRequest(custom_mode='OFFBOARD')
    arm_cmd = CommandBoolRequest(value=True)

    last_req = rospy.Time.now()

    while not rospy.is_shutdown():
        now = rospy.Time.now()

        # Only try to switch to OFFBOARD if not already in it and not RTL
        if current_state.mode != "OFFBOARD" and current_state.mode != "AUTO.RTL" and (now - last_req > rospy.Duration(5.0)):
            if set_mode_client.call(offb_set_mode).mode_sent:
                rospy.loginfo("OFFBOARD enabled")
            last_req = now

        # Try to arm
        elif not current_state.armed and current_state.mode !="AUTO.RTL" and (now - last_req > rospy.Duration(5.0)):
            if arming_client.call(arm_cmd).success:
                rospy.loginfo("Vehicle armed")
            last_req = now

        # Only publish setpoints if still in OFFBOARD (not RTL)
        if current_state.mode == "OFFBOARD":
            local_pos_pub.publish(pose)

        rate.sleep()
