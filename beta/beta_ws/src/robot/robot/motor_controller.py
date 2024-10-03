import rclpy
from rclpy.node import Node
from math import pi
from numpy import interp

from robot_interfaces.msg import DutyCycle
from geometry_msgs.msg import Twist


class MotorController(Node):

    def __init__(self):
        super().__init__('motor_controller')
        self.cmd_vel_subscription = self.create_subscription(Twist, 'cmd_vel', self.listener_callback, 10)
        self.cmd_vel_subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(DutyCycle, 'duty_cycle', 10)
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.max_rpm = 60.0
        self.wheel_base = 0.295
        self.wheel_radius = 0.060
        self.duty_cycle_left = 0.0
        self.duty_cycle_right = 0.0 

    def listener_callback(self, msg):
        speed = msg.linear.x
        spin = msg.angular.z
        linear_velocity_left = (speed - (spin * self.wheel_base / 2.0)) / (self.wheel_radius)
        linear_velocity_right = (speed + (spin * self.wheel_base / 2.0)) / (self.wheel_radius)
        target_rpm_left = (linear_velocity_left * 60.0) / (pi * 2.0)
        target_rpm_right = (linear_velocity_right * 60.0) / (pi * 2.0)
        percentage_left = (target_rpm_left / self.max_rpm) * 100.0
        percentage_right = (target_rpm_right / self.max_rpm) * 100.0
        self.duty_cycle_left = interp(percentage_left, [-100, 100], [10.50, 19.50])
        self.duty_cycle_right = interp(percentage_right, [-100, 100], [10.50, 19.50])

    def timer_callback(self):
        msg = DutyCycle()
        msg.duty_cycle_left = self.duty_cycle_left
        msg.duty_cycle_right = self.duty_cycle_right
        self.publisher_.publish(msg)


def main(args=None):
    print('Publishing duty_cycle...')
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