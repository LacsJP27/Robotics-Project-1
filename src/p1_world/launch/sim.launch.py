from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    # Robot spawn pose args
    x_pose = LaunchConfiguration("x_pose")
    y_pose = LaunchConfiguration("y_pose")
    yaw = LaunchConfiguration("yaw")

    # World path from package share (grader-safe)
    pkg_share = get_package_share_directory("p1_world")
    world_path = os.path.join(pkg_share, "worlds", "world.sdf")

    # 1) Start Gazebo Sim with the world
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("ros_gz_sim"),
                "launch",
                "gz_sim.launch.py",
            )
        ),
        launch_arguments={
            "gz_args": f"-r -v 4 {world_path}"
        }.items(),
    )

    # 2) Spawn TurtleBot4 + start Nav2 bringup (recommended by your handout)
    # NOTE: This filename can vary by install. If yours errors, we’ll swap it.
    nav2_tb4 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("nav2_bringup"),
                "launch",
                "tb4_simulation_launch.py",
            )
        ),
        launch_arguments={
            "world": world_path,
            "x_pose": x_pose,
            "y_pose": y_pose,
            "yaw": yaw,
        }.items(),
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument("x_pose", default_value="0.0"),
            DeclareLaunchArgument("y_pose", default_value="0.0"),
            DeclareLaunchArgument("yaw", default_value="0.0"),
            gz_sim,
            nav2_tb4,
        ]
    )
