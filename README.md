run the following command in the root directory to build package
```
colcon build
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
