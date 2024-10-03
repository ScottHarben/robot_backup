import os
from ament_index_python.packages import get_package_share_directory
from launch_ros.substitutions import FindPackageShare
import launch
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution

def generate_launch_description():
    
    #robot description
    default_model_path = os.path.join(get_package_share_directory("robot_description"),
                                     'robot_description.urdf')
    
    return launch.LaunchDescription([
        
        #robot description
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
            name='joint_state_publisher'),

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
            executable='velocity_publisher'),

        Node(
            package='robot',
            executable='motor_controller'),

        Node(
            package='robot',
            executable='pid_controller'),

        Node(
            package='robot',
            executable='motor_driver'),

        Node(
            package='robot',
            executable='odom_publisher'),

        Node(
            package='robot',
            executable='imu_controller'),

        # Node(
        #     package = "realsense2_camera",
        #     executable="realsense2_camera_node",
        #     name="camera",
        #     output="screen",
        #     parameters=[
        #         {"enable_accel": True},
        #         {"enable_gyro": True},
        #         {"unite_imu_method": 1},
        #         {"pointcloud.enable": True}
        #     ]),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('realsense2_camera'),
                    'launch',
                    'rs_launch.py'
                ])
            ]),
            launch_arguments={
                'enable_accel': 'true',
                'enable_gyro': 'true',
                'unite_imu_method': '1',
                'pointcloud.enable': 'true'
            }.items()
        ),
        

        Node(
            package = "imu_filter_madgwick",
            executable="imu_filter_madgwick_node",
            name="imu_filter",
            output="screen",
            parameters=[os.path.join(
                        get_package_share_directory('robot_bringup'),
                        'config',
                        'imu_filter_madgwick_params.yaml')]),

        Node(
            package = "robot_localization",
            executable="ekf_node",
            name="ekf_filter_node",
            output="screen",
            parameters=[os.path.join(
                        get_package_share_directory('robot_bringup'),
                        'config',
                        'ekf_params.yaml')])
  ])