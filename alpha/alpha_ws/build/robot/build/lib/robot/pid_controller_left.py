import rclpy
from rclpy.node import Node
import math
from numpy import interp

from robot_interfaces.msg import DutyCycle, WheelRPM


class PidControllerLeft(Node):

    def __init__(self):
        super().__init__('pid_controller_left')
        self.target_velocity_subscription = self.create_subscription(WheelRPM, 'target_rpm', self.target_rpm_callback, 10)
        self.target_velocity_subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(DutyCycle, 'duty_cycle_left', 10)
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.max_rpm = 60.0
        self.wheel_diameter = 0.120
        self.duty_cycle = 0.0

    def target_rpm_callback(self, msg):
        percentage = (msg.rpm_left / self.max_rpm) * 100.0
        self.duty_cycle = interp(percentage, [-100, 100], [210, 390])

    def timer_callback(self):
        msg = DutyCycle()
        msg.duty_cycle_left = self.duty_cycle
        self.publisher_.publish(msg)


def main(args=None):
    print('Publishing duty_cycle...')
    rclpy.init(args=args)
    pid_controller_left = PidControllerLeft()
    rclpy.spin(pid_controller_left)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    pid_controller_left.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()