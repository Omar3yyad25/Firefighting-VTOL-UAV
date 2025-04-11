#!/bin/bash

echo "[INFO] Publishing dummy setpoints in background..."

# Start publishing setpoints at 10Hz
rostopic pub -r 10 /mavros/setpoint_position/local geometry_msgs/PoseStamped "header:
  frame_id: 'map'
pose:
  position:
    x: 2.0
    y: 2.0
    z: 2.0" &

# Give it 5 seconds to warm up
sleep 5

echo "[INFO] Attempting to switch to OFFBOARD mode..."
rosservice call /mavros/set_mode "base_mode: 0
custom_mode: 'OFFBOARD'"

echo "[INFO] Attempting to arm..."
rosservice call /mavros/cmd/arming "value: true"

echo "[INFO] Done."
