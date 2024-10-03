import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import UnlessCondition
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    #lidar
    serial_port = LaunchConfiguration('serial_port', default='/dev/ttyUSB0')
    serial_baudrate = LaunchConfiguration('serial_baudrate', default='115200') #for A1/A2 is 115200
    frame_id = LaunchConfiguration('frame_id', default='laser')
    inverted = LaunchConfiguration('inverted', default='false')
    angle_compensate = LaunchConfiguration('angle_compensate', default='true')

    #robot description
    default_model_path = os.path.join(get_package_share_directory("robot_description"),
                                     'src/description', 'robot_description.urdf')

    return LaunchDescription([

        #lidar
        DeclareLaunchArgument(
            'serial_port',
            default_value=serial_port,
            description='Specifying usb port to connected lidar'),

        DeclareLaunchArgument(
            'serial_baudrate',
            default_value=serial_baudrate,
            description='Specifying usb port baudrate to connected lidar'),
        
        DeclareLaunchArgument(
            'frame_id',
            default_value=frame_id,
            description='Specifying frame_id of lidar'),

        DeclareLaunchArgument(
            'inverted',
            default_value=inverted,
            description='Specifying whether or not to invert scan data'),

        DeclareLaunchArgument(
            'angle_compensate',
            default_value=angle_compensate,
            description='Specifying whether or not to enable angle_compensate of scan data'),

        Node(
            package='rplidar_ros2',
            executable='rplidar_scan_publisher',
            name='rplidar_scan_publisher',
            parameters=[{'serial_port': serial_port, 
                         'serial_baudrate': serial_baudrate, 
                         'frame_id': frame_id,
                         'inverted': inverted, 
                         'angle_compensate': angle_compensate}],
            output='screen'),

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
            package="robot",
            executable="imu"),

        Node(
            package="robot",
            executable="encoder"),

        Node(
            package="robot",
            executable="motor"),

        Node(
            package="robot",
            executable="odom"),

        Node(
            package = "robot_localization",
            executable="ekf_node",
            name="ekf_filter_node",
            output="screen",
            parameters=[os.path.join(
                        get_package_share_directory('robot_bringup'),
                        'params',
                        'ekf_params.yaml')]),

        #static transform
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments = ['0', '0', '1', '0', '0', '0', 'map', 'odom'])
    ])
