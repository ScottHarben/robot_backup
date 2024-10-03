#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

import tf2_ros
from robot_interfaces.msg import DualEncoder
from geometry_msgs.msg import Twist, TransformStamped
from nav_msgs.msg import Odometry
from math import cos, sin
from scipy.spatial.transform import Rotation


class OdomPublisher(Node):

    def __init__(self):
        super().__init__('odom0')
        self.cmd_vel_subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.cmd_vel_callback,
            10)
        self.encoder_pub_subscription = self.create_subscription(
            DualEncoder,
            'encoder_pub',
            self.encoder_pub_callback,
            10)
        self.cmd_vel_subscription
        self.encoder_pub_subscription

        self.publisher_ = self.create_publisher(Odometry, 'odom_pub', 10)
        self.timer_ = self.create_timer(0.1, self.publish_odom)
        
        self.current_time = self.get_clock().now()
        self.last_time = self.get_clock().now()
        
        self.x = 0
        self.y = 0
        self.th = 0
        
        self.motor_left_direction = 1
        self.motor_right_direction = 1
        
        self.left_count = 0
        self.right_count = 0
        self.prev_left_count = 0
        self.prev_right_count = 0
        
        self.odom_transform = TransformStamped()
        self.odom = Odometry()

    def cmd_vel_callback(self, data):
        x = data.linear.x
        z = data.angular.z
        if x == 0 and z == 0:
            self.motor_left_direction = self.motor_left_direction
            self.motor_right_direction = self.motor_right_direction
        elif x != 0:
            if x > 0:
                self.motor_left_direction = 1
                self.motor_right_direction = 1
            else:
                self.motor_left_direction = -1
                self.motor_right_direction = -1
        else:
            if z > 0:
                self.motor_left_direction = -1
                self.motor_right_direction = 1
            else:
                self.motor_left_direction = 1
                self.motor_right_direction = -1

    def encoder_pub_callback(self, data):
        self.left_count += (data.left_count * self.motor_left_direction)
        self.right_count += (data.right_count * self.motor_right_direction)
                            
    def create_odom(self):
        self.current_time = self.get_clock().now()
        distance_per_tick = 0.01035
        dist_between_wheels = 0.133
        delta_left = self.left_count - self.prev_left_count
        delta_right = self.right_count - self.prev_right_count
        dt = (self.current_time - self.last_time).nanoseconds/1e9
        omega_left = (delta_left * distance_per_tick) / dt
        omega_right = (delta_right * distance_per_tick) / dt
        vx = (omega_right + omega_left) / 2
        vy = 0.0
        vth = (omega_right - omega_left) / dist_between_wheels
        delta_x = (vx * cos(self.th)) * dt
        delta_y = (vx * sin(self.th)) * dt
        delta_th = vth * dt
        self.x += delta_x
        self.y += delta_y
        self.th += delta_th
        rot = Rotation.from_euler('xyz', [0,0,self.th], degrees=False)
        odom_quaternion = rot.as_quat()
        
        self.odom_transform.header.stamp = self.current_time.to_msg()
        self.odom_transform.header.frame_id = "odom"
        self.odom_transform.child_frame_id = "base_link"
        self.odom_transform.transform.translation.x = self.x
        self.odom_transform.transform.translation.y = self.y
        self.odom_transform.transform.translation.z = 0.0
        self.odom_transform.transform.rotation.x = odom_quaternion[0]
        self.odom_transform.transform.rotation.y = odom_quaternion[1]
        self.odom_transform.transform.rotation.z = odom_quaternion[2]
        self.odom_transform.transform.rotation.w = odom_quaternion[3]
        
        self.odom.header.stamp = self.current_time.to_msg()
        self.odom.header.frame_id = "odom"
        self.odom.child_frame_id = "base_link"
        self.odom.pose.pose.position.x = self.x
        self.odom.pose.pose.position.y = self.y
        self.odom.pose.pose.position.z = 0.0
        self.odom.pose.pose.orientation.x = odom_quaternion[0]
        self.odom.pose.pose.orientation.y = odom_quaternion[1]
        self.odom.pose.pose.orientation.z = odom_quaternion[2]
        self.odom.pose.pose.orientation.w = odom_quaternion[3]
        self.odom.twist.twist.linear.x = vx
        self.odom.twist.twist.linear.y = vy
        self.odom.twist.twist.angular.z = vth
        
        self.prev_left_count = self.left_count
        self.prev_right_count = self.right_count
        self.last_time = self.current_time

    def publish_odom(self):
        # odom_broadcaster = tf2_ros.TransformBroadcaster(self)
        # odom_broadcaster.sendTransform(self.odom_transform)
        self.create_odom()
        self.publisher_.publish(self.odom)
        

def main(args=None):
    rclpy.init(args=args)
    odom_publisher = OdomPublisher()
    print("publishing encoder odom")
    rclpy.spin(odom_publisher)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
