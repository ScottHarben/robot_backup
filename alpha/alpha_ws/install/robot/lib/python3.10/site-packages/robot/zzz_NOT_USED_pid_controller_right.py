import rclpy
from rclpy.node import Node
import math
from numpy import interp
from simple_pid import PID

from robot_interfaces.msg import DutyCycle, WheelRPM


class PidControllerRight(Node):

    def __init__(self):
        super().__init__('pid_controller_right')
        self.target_velocity_subscription = self.create_subscription(WheelRPM, 'target_rpm', self.target_rpm_callback, 10)
        self.target_velocity_subscription  # prevent unused variable warning

        self.feedback_velocity_subscription = self.create_subscription(WheelRPM, 'feedback_rpm_right', self.feedback_rpm_callback, 10)
        self.feedback_velocity_subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(DutyCycle, 'duty_cycle_right', 10)
        
        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.feedback_rpm = 0.0
        self.max_rpm = 60.0
        self.wheel_diameter = 0.120
        self.duty_cycle = 0.0

        Kp = 0.15
        Ki = 2.5
        Kd = 0.03
        output_limit = self.max_rpm # max mps to avoid runaway pid output
        self.pid = PID(Kp, Ki, Kd, setpoint=0)
        self.pid.output_limits = (0.0 - output_limit, output_limit)

    def feedback_rpm_callback(self, msg):
        self.feedback_rpm = msg.rpm_right

    def target_rpm_callback(self, msg):
        self.pid.setpoint = msg.rpm_right
        pid_rpm = self.pid(self.feedback_rpm)
        percentage = (pid_rpm / self.max_rpm) * 100.0
        
        self.duty_cycle = interp(percentage, [-100, 100], [210, 390])

    def timer_callback(self):
        msg = DutyCycle()
        msg.duty_cycle_right = self.duty_cycle
        self.publisher_.publish(msg)


def main(args=None):
    print('Publishing duty_cycle_right...')
    rclpy.init(args=args)
    pid_controller_right = PidControllerRight()
    rclpy.spin(pid_controller_right)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    pid_controller_right.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()