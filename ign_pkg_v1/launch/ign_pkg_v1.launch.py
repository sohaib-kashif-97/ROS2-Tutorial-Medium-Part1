import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    package_name = 'ign_pkg_v1'
    share_dir = get_package_share_directory(package_name)
    world_path = os.path.join('worlds', 'world.sdf')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['ign', 'gazebo', world_path, '--verbose'],
            cwd=share_dir,
            output='screen'
        ),
    ])