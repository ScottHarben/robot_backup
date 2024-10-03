#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Imu
from geometry_msgs.msg import PoseStamped
import board
import adafruit_bno055

i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c)

class ImuPublisher(Node):

    def __init__(self):
        super().__init__('imu0')
        self.publisher_ = self.create_publisher(Imu, 'imu_pub', 10)
        #self.pose_publisher_ = self.create_publisher(PoseStamped, 'pose_pub', 10)
        self.timer_ = self.create_timer(0.1, self.publish_imu)

    def publish_imu(self):
        msg = Imu()
        msg.header.frame_id = 'base_link'
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.orientation.w = sensor.quaternion[0]
        msg.orientation.x = sensor.quaternion[1]
        msg.orientation.y = sensor.quaternion[2]
        msg.orientation.z = sensor.quaternion[3]
        #msg.linear_acceleration.x = sensor.acceleration[0]
        #msg.linear_acceleration.y = sensor.acceleration[1]
        #msg.linear_acceleration.z = sensor.acceleration[2]
        msg.linear_acceleration_covariance[0] = -1
        #msg.angular_velocity.x = sensor.gyro[0]
        #msg.angular_velocity.y = sensor.gyro[1]
        #msg.angular_velocity.z = sensor.gyro[2]
        msg.angular_velocity_covariance[0] = -1
        self.publisher_.publish(msg)
        
        #pose = PoseStamped()
        #pose.header.frame_id = 'odom'
        #pose.header.stamp = self.get_clock().now().to_msg()
        #pose.pose.orientation.w = sensor.quaternion[0]
        #pose.pose.orientation.x = sensor.quaternion[1]
        #pose.pose.orientation.y = sensor.quaternion[2]
        #pose.pose.orientation.z = sensor.quaternion[3]
        #pose.pose.position.x = 0.0
        #pose.pose.position.y = 0.0
        #pose.pose.position.z = 0.0
        #self.pose_publisher_.publish(pose)

def main(args=None):
    rclpy.init(args=args)
    imu_publisher = ImuPublisher()
    print("publishing imu")
    rclpy.spin(imu_publisher)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
