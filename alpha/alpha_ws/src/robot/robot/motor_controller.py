import rclpy
from math import pi
from rclpy.node import Node

from robot_interfaces.msg import WheelRPM
from geometry_msgs.msg import Twist


class MotorController(Node):

    def __init__(self):
        super().__init__('motor_controller')
        self.cmd_vel_subscription = self.create_subscription(Twist, 'cmd_vel', self.listener_callback, 10)
        self.cmd_vel_subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(WheelRPM, 'target_rpm', 10)
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.wheel_base = 0.338
        self.wheel_radius = 0.060
        self.target_rpm_left = 0.0
        self.target_rpm_right = 0.0

    def listener_callback(self, msg):
        speed = msg.linear.x
        spin = msg.angular.z
        linear_velocity_left = (speed - (spin * self.wheel_base / 2.0)) / (self.wheel_radius)
        linear_velocity_right = (speed + (spin * self.wheel_base / 2.0)) / (self.wheel_radius)
        self.target_rpm_left = (linear_velocity_left * 60.0) / (pi * 2.0)
        self.target_rpm_right = (linear_velocity_right * 60.0) / (pi * 2.0)

    def timer_callback(self):
        msg = WheelRPM()
        msg.rpm_left = self.target_rpm_left
        msg.rpm_right = self.target_rpm_right
        self.publisher_.publish(msg)


def main(args=None):
    print('Publishing target_rpm...')
    rclpy.init(args=args)
    motor_controller = MotorController()
    rclpy.spin(motor_controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    motor_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()