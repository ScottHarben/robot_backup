import launch
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return launch.LaunchDescription([
        #robot
        Node(
            package='robot',
            executable='motor_controller'),

        Node(
            package='robot',
            executable='motor_driver'),

    ])
