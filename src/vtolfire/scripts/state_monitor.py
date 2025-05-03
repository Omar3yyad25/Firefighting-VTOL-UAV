#!/usr/bin/env python3

import rospy
from mavros_msgs.msg import State

# Callback function to handle state data
def state_callback(data):
    rospy.loginfo("Current Mode: %s", data.mode)
    rospy.loginfo("Connected: %s", data.connected)

def state_monitoring_node():
    # Initialize the node
    rospy.init_node('state_monitoring_node', anonymous=True)

    # Subscribe to the /mavros/state topic
    rospy.Subscriber("/mavros/state", State, state_callback)

    # Spin to keep the node running
    rospy.spin()

if __name__ == '__main__':
    try:
        state_monitoring_node()
    except rospy.ROSInterruptException:
        pass
