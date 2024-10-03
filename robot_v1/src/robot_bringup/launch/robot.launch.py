import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    imu_node = Node(
        package="robot",
        executable="imu",
    )

    encoder_node = Node(
        package="robot",
        executable="encoder"
    )

    motor_node = Node(
        package="robot",
        executable="motor"
    )

    odom_node = Node(
        package="robot",
        executable="odom"
    )

    ekf_params = os.path.join(
        get_package_share_directory('robot_bringup'),
        'params',
        'ekf_params.yaml'
    )

    ekf_node = Node(
        package = "robot_localization",
        executable="ekf_node",
        name="ekf_filter_node",
        output="screen",
        parameters=[ekf_params]
    )

    ld.add_action(imu_node)
    ld.add_action(encoder_node)
    ld.add_action(motor_node)
    ld.add_action(odom_node)
    ld.add_action(ekf_node)

    return ld
