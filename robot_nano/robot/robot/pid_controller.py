import rclpy
from rclpy.node import Node
import math
from numpy import interp
from simple_pid import PID

from robot_interfaces.msg import DutyCycle, WheelVelocity


class PidController(Node):

    def __init__(self):
        super().__init__('pid_controller')
        self.target_velocity_subscription = self.create_subscription(WheelVelocity, 'target_velocity', self.target_velocity_callback, 10)
        self.target_velocity_subscription  # prevent unused variable warning

        self.feedback_velocity_subscription = self.create_subscription(WheelVelocity, 'feedback_velocity', self.feedback_velocity_callback, 10)
        self.feedback_velocity_subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(DutyCycle, 'duty_cycle', 10)
        
        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.feedback_velocity_left = 0.0
        self.feedback_velocity_right = 0.0

        self.max_rpm = 60.0
        self.wheel_diameter = 0.135
        self.duty_cycle_left = 0.0
        self.duty_cycle_right = 0.0

        # Kp = 0.1
        # Ki = 3.0
        # Kd = 0.0
        # output_limit = 0.43 # max mps to avoid runaway pid output
        # self.pid_left = PID(Kp, Ki, Kd, setpoint=0)
        # self.pid_left.output_limits = (0.0 - output_limit, output_limit)
        # self.pid_right = PID(Kp, Ki, Kd, setpoint=0)
        # self.pid_right.output_limits = (0.0 - output_limit, output_limit)

    def feedback_velocity_callback(self, msg):
        self.feedback_velocity_left = msg.linear_velocity_left
        self.feedback_velocity_right = msg.linear_velocity_right

    def target_velocity_callback(self, msg):
        # self.pid_left.setpoint = msg.linear_velocity_left
        # self.pid_right.setpoint = msg.linear_velocity_right
        # pid_velocity_left = self.pid_left(self.feedback_velocity_left)
        # pid_velocity_right = self.pid_right(self.feedback_velocity_right)
        # target_rpm_left = (pid_velocity_left * 60.0) / (math.pi * self.wheel_diameter)
        # target_rpm_right = (pid_velocity_right * 60.0) / (math.pi * self.wheel_diameter)
        target_rpm_left = (msg.linear_velocity_left * 60.0) / (math.pi * self.wheel_diameter)
        target_rpm_right = (msg.linear_velocity_right * 60.0) / (math.pi * self.wheel_diameter)
        percentage_left = (target_rpm_left / self.max_rpm) * 100.0
        percentage_right = (target_rpm_right / self.max_rpm) * 100.0
        percentage_left = max(min(percentage_left, 100.0), -100.0)
        percentage_right = max(min(percentage_right, 100.0), -100.0)
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
    pid_controller = PidController()
    rclpy.spin(pid_controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    pid_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()