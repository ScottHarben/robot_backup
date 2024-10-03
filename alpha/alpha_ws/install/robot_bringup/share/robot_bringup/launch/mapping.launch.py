import os
import launch
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    bringup_dir = get_package_share_directory('robot_bringup')
    launch_dir = os.path.join(bringup_dir, 'launch')

    odom_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(launch_dir, 'odom.launch.py')))

    online_async_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(launch_dir, 'online_async_launch.py')))

    # Create the launch description and populate
    ld = LaunchDescription()

    # Add the actions to launch all of the navigation nodes
    ld.add_action(odom_launch)
    ld.add_action(online_async_launch)

    return ld