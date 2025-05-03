#!/usr/bin/env python3

import rospy
from mavros_msgs.srv import SetMode, SetModeRequest
from std_msgs.msg import Empty

def rtl_callback(msg):
    rospy.loginfo("RTL command received.")
    try:
        rtl_set_mode = SetModeRequest()
        rtl_set_mode.custom_mode = "AUTO.RTL"

        response = set_mode_srv(rtl_set_mode)
        if response.mode_sent:
            rospy.loginfo("RTL mode set successfully.")
        else:
            rospy.logwarn("Failed to set RTL mode.")
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")

if __name__ == "__main__":
    rospy.init_node("rtl_node")

    rospy.wait_for_service("/mavros/set_mode")
    set_mode_srv = rospy.ServiceProxy("/mavros/set_mode", SetMode)

    rospy.Subscriber("/rtl_trigger", Empty, rtl_callback)

    rospy.loginfo("RTL node is ready and waiting for trigger...")

    rospy.spin()

