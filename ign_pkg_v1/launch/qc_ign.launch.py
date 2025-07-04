import os
from launch import LaunchDescription
#from launch_ros.actions import Node
from launch.actions import ExecuteProcess, IncludeLaunchDescription

def generate_launch_description():
    package_name = 'qc_ign_v1'
    world_file = 'worlds/world.sdf'
    
    world_path = os.path.join(
        os.path.expanduser('~/ROS2/CPP Packages/ros2_ws/src'), package_name, world_file
    )

    return LaunchDescription([
        ExecuteProcess(
            cmd=['ign', 'gazebo', world_path, '--verbose'],
            output='screen'
        ),
        
    ])

