run the following command in the root directory (ros2_ws) to build package
```
colcon build --symlink-install
```

Then source ros in new terminal
```
source install/setup.bash
```

Run world package
```
 ros2 launch p1_world tb4_in_world.launch.py
```
Run controller in new terminal
```
ros2 run project1_control controller
```

For keyboard control:
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/cmd_vel_key
```

To just view the world.sdf file
cd into the worlds directory
```
gz sim world.sdf
```



Set up and fixed all of the package and folder struture and the colcon build works. -Avi

Notes from class
- package for project1
- package for project1_controller (later part of project)
- consider launch configs in world launch file
- pass launch configs to launch description
- declare the controller node in this file so the file can use the package
- Controller_node.py
  - rclpy library
  - define the node (import Node from rclpy.node)
  - new class called Project1Controller, basically a ros2 node with other methods
  - 
