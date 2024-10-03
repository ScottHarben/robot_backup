import rclpy
from rclpy.node import Node

from robot_interfaces.msg import WheelVelocity
from geometry_msgs.msg import Twist


class MotorController(Node):

    def __init__(self):
        super().__init__('motor_controller')
        self.cmd_vel_subscription = self.create_subscription(Twist, 'cmd_vel', self.listener_callback, 10)
        self.cmd_vel_subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(WheelVelocity, 'target_velocity', 10)
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.speed = 0.0
        self.spin = 0.0
        self.wheel_base = 0.262
        self.wheel_diameter = 0.135
        self.linear_velocity_left = 0.0
        self.linear_velocity_right = 0.0

    def listener_callback(self, msg):
        self.speed = msg.linear.x
        self.spin = msg.angular.z
        twist_mps_left= -1.0 * self.spin * self.wheel_base / self.wheel_diameter
        twist_mps_right = self.spin * self.wheel_base / self.wheel_diameter
        self.linear_velocity_left = self.speed + twist_mps_left
        self.linear_velocity_right = self.speed + twist_mps_right

    def timer_callback(self):
        msg = WheelVelocity()
        msg.linear_velocity_left = self.linear_velocity_left
        msg.linear_velocity_right = self.linear_velocity_right
        self.publisher_.publish(msg)


def main(args=None):
    print('Publishing target_velocity...')
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