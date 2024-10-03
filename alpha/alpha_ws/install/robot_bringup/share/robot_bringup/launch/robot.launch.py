import os
import launch
from ament_index_python import get_package_share_directory
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution

def generate_launch_description():
    return launch.LaunchDescription([
        #robot
        Node(
            package='robot',
            executable='encoder_publisher_left'),

        Node(
            package='robot',
            executable='encoder_publisher_right'),

        Node(
            package='robot',
            executable='encoder_publisher'),

        Node(
            package='robot',
            executable='motor_controller'),

        Node(
            package='robot',
            executable='pid_controller_left'),

        Node(
            package='robot',
            executable='pid_controller_right'),

        Node(
            package='robot',
            executable='motor_driver'),

        # Node(
        #     package='robot',
        #     executable='odom_publisher')

    ])
