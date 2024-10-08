import os
import launch
from ament_index_python import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import Command, LaunchConfiguration
from launch.conditions import UnlessCondition

def generate_launch_description():

    #robot description
    default_model_path = os.path.join(get_package_share_directory("robot_description"),
                                    'robot_description.urdf')

    return launch.LaunchDescription([

        #robot description
        DeclareLaunchArgument(
            name='gui', 
            default_value='False',
            description='Flag to enable joint_state_publisher_gui'),

        DeclareLaunchArgument(
            name='model', 
            default_value=default_model_path,
            description='Absolute path to robot urdf file'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': Command(['xacro ', LaunchConfiguration('model')])}]),

        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            condition=UnlessCondition(LaunchConfiguration('gui'))),

        #robot
        Node(
            package='robot',
            executable='motor_controller'),

        Node(
            package='robot',
            executable='motor_driver')

    ])
