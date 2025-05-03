#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from std_msgs.msg import Bool
import cv2
import numpy as np
import os

# ==== Parameters ====
TARGET_POS = (2.0, 2.0, 2.0)
POS_TOLERANCE = 0.2
IMAGE_PATH = "/home/omar/catkin_ws/src/vtolfire/scripts/input/fire.jpeg"
OUTPUT_FOLDER = "/home/omar/catkin_ws/src/vtolfire/scripts/output"
PIXEL_TO_METER_SCALE = 0.01
IMAGE_CENTER = (800, 506)


# ==== Global Variables ====
setpoint_pub = None
override_pub = None
camera_triggered = False


def detect_hottest_contour_and_save(image_path, threshold=200, blur_kernel=5):
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    img = cv2.imread(image_path)
    if img is None:
        rospy.logerr(f"Could not load image from {image_path}")
        return (0, 0)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (blur_kernel, blur_kernel), 0)
    _, thresh = cv2.threshold(blurred, threshold, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    highest_score = -1
    highest_contour = None
    highest_center = (0, 0)

    for contour in contours:
        mask = np.zeros_like(gray, dtype=np.uint8)
        cv2.drawContours(mask, [contour], -1, color=255, thickness=-1)
        score = cv2.mean(blurred, mask=mask)[0]
        if score > highest_score:
            highest_score = score
            highest_contour = contour

    if highest_contour is not None:
        M = cv2.moments(highest_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            highest_center = (cx, cy)
            rospy.loginfo(f"Hottest spot at (pixel): x={cx}, y={cy}")
        else:
            rospy.logwarn("Zero division error in moment calculation.")
    else:
        rospy.logwarn("No hotspot detected in image.")

    return highest_center


def position_callback(msg):
    global camera_triggered, setpoint_pub, override_pub

    px = msg.pose.position.x
    py = msg.pose.position.y
    pz = msg.pose.position.z

    if (abs(px - TARGET_POS[0]) < POS_TOLERANCE and
        abs(py - TARGET_POS[1]) < POS_TOLERANCE and
        abs(pz - TARGET_POS[2]) < POS_TOLERANCE):

        if not camera_triggered:
            camera_triggered = True
            rospy.loginfo("Target position reached. Running fire detection...")

            hotspot_center = detect_hottest_contour_and_save(IMAGE_PATH)
            cx, cy = hotspot_center

            x_offset = (cx - IMAGE_CENTER[0]) * PIXEL_TO_METER_SCALE
            y_offset = (cy - IMAGE_CENTER[1]) * PIXEL_TO_METER_SCALE

            new_pose = PoseStamped()
            new_pose.header.stamp = rospy.Time.now()
            new_pose.header.frame_id = "map"
            new_pose.pose.position.x = px + x_offset
            new_pose.pose.position.y = py + y_offset
            new_pose.pose.position.z = pz

            # Notify other nodes to stop their publishing
            override_msg = Bool(data=True)
            override_pub.publish(override_msg)
            rospy.loginfo(f"New setpoints: x= {new_pose.pose.position.x:.2f}, y= {new_pose.pose.position.y:.2f}")

            rospy.loginfo("Override activated. Publishing new fire setpoints...")

            rate = rospy.Rate(20)
            while not rospy.is_shutdown():
                setpoint_pub.publish(new_pose)
                target_pub.publish(new_pose)
                rate.sleep()


def fire_detection_node():
    global setpoint_pub, override_pub, target_pub

    rospy.init_node("fire_detection_node")
    target_pub = rospy.Publisher("/fire_hotspot_target", PoseStamped, queue_size=1)
    rospy.Subscriber("/mavros/local_position/pose", PoseStamped, position_callback)
    setpoint_pub = rospy.Publisher("/mavros/setpoint_position/local", PoseStamped, queue_size=10)
    override_pub = rospy.Publisher("/fire_detection/override_active", Bool, queue_size=1)

    rospy.loginfo("🔥 Fire Detection Node is running...")
    rospy.spin()


if __name__ == "__main__":
    fire_detection_node()