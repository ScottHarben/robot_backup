import os
import launch
from launch_ros.actions import Node

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
            executable='motor_driver'), 
        Node(
            package='robot',
            executable='t1_direction_publisher'), 
        Node(
            package='robot',
            executable='t1_distance_publisher'), 
        Node(
            package='robot',
            executable='t1_servo_controller'), 
        Node(
            package='robot',
            executable='t2_direction_publisher'), 
        Node(
            package='robot',
            executable='t2_distance_publisher'), 
        Node(
            package='robot',
            executable='t2_servo_controller'), 
      ])
