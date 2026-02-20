
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    pkg_path = get_package_share_directory('p1_world')
    world_path = os.path.join(pkg_path, 'worlds', 'world.sdf')

    gazebo = ExecuteProcess(
        cmd=['gz', 'sim', world_path],
        output='screen'
    )

    return LaunchDescription([
        gazebo
    ])

