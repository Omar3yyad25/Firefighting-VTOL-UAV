#!/usr/bin/env python3
 
import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.srv import CommandLong, CommandLongRequest
import math
import time

# ─────────────── PARAMETERS ───────────────
SERVO_ID            = rospy.get_param("/ball_deploy/servo_id", 9)      # PX4 AUX1 = servo channel 9
SERVO_OPEN_PWM      = rospy.get_param("/ball_deploy/open_pwm", 1900)  # PWM value to open gate
POS_TOLERANCE_M     = rospy.get_param("/ball_deploy/pos_tol", 0.30)   # meters tolerance
MAV_CMD_DO_SET_SERVO = 183  # MAVLink command ID for DO_SET_SERVO
 
# ─────────────── STATE ────────────────────
target_pose = None
current_pose = None
deployed = False
last_log_time = 0.0
 
# ─────────────── CALLBACKS ────────────────
def hotspot_cb(msg: PoseStamped):
    global target_pose
    target_pose = msg
 
def position_cb(msg: PoseStamped):
    global current_pose
    current_pose = msg
    _check_and_deploy()
 
# ─────────────── LOGIC ────────────────────
def _reached_target() -> bool:
    if not target_pose or not current_pose:
        return False
    dx = current_pose.pose.position.x - target_pose.pose.position.x
    dy = current_pose.pose.position.y - target_pose.pose.position.y
    dz = current_pose.pose.position.z - target_pose.pose.position.z
    return math.sqrt(dx*dx + dy*dy + dz*dz) <= POS_TOLERANCE_M
 
def _send_servo_command():
    rospy.wait_for_service("/mavros/cmd/command")
    servo_srv = rospy.ServiceProxy("/mavros/cmd/command", CommandLong)
 
    req = CommandLongRequest()
    req.command = MAV_CMD_DO_SET_SERVO
    req.param1  = SERVO_ID
    req.param2  = SERVO_OPEN_PWM
 
    resp = servo_srv(req)
    if resp.success:
        rospy.loginfo(f"Ball deployed: servo {SERVO_ID} → PWM {SERVO_OPEN_PWM}")
    else:
        rospy.logwarn("Failed to send servo command")
 
def _check_and_deploy():
    global deployed, last_log_time
    now = time.time()

    if not deployed and _reached_target():
        rospy.loginfo(f"🏀 Deployment location reached: {target_pose.pose.position.x},{target_pose.pose.position.y},{target_pose.pose.position.z}")
        rospy.loginfo("🏀 Deploying ball...")
        _send_servo_command()
        deployed = True

    elif not deployed and target_pose and (now - last_log_time) >= 1.5:
        last_log_time = now
        rospy.loginfo("❗ Waiting to reach deployment location...")
        rospy.loginfo(f"❗ Current position: {current_pose.pose.position.x},{current_pose.pose.position.y},{current_pose.pose.position.z}")
    
        distance = math.sqrt(
            (current_pose.pose.position.x - target_pose.pose.position.x) ** 2 +
            (current_pose.pose.position.y - target_pose.pose.position.y) ** 2 +
            (current_pose.pose.position.z - target_pose.pose.position.z) ** 2
        )
        rospy.loginfo(f"❗ Target position: {target_pose.pose.position.x},{target_pose.pose.position.y},{target_pose.pose.position.z}")
        rospy.loginfo(f"❗ Distance to target: {distance:.2f} m")


# ─────────────── NODE SETUP ──────────────
def main():
    rospy.init_node("ball_deploy_node")
 
    rospy.Subscriber("/fire_hotspot_target", PoseStamped, hotspot_cb)
    rospy.Subscriber("/mavros/local_position/pose", PoseStamped, position_cb)
 
    rospy.loginfo("Ball Deploy Node running, waiting for hotspot…")
    rospy.spin()
 
if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass