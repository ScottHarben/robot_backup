import rclpy
from math import pi
from rclpy.node import Node

from geometry_msgs.msg import Twist
from robot_interfaces.msg import TickCount, DutyCycle


class MotorController(Node):

    def __init__(self):
        super().__init__('motor_controller')
        self.cmd_vel_subscription = self.create_subscription(Twist, 'cmd_vel', self.cmd_vel_callback, 10)
        self.cmd_vel_subscription  # prevent unused variable warning
        self.encoder_publisher_subscription = self.create_subscription(TickCount, 'encoder_ticks', self.encoder_publisher_callback, 10)
        self.encoder_publisher_subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(DutyCycle, 'duty_cycle', 10)
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.motor_direction_forward = 1
        self.motor_direction_backward = -1
        self.motor_direction_left = 1
        self.motor_direction_right = 1
        self.motor_on_left = 0
        self.motor_on_right = 0
        self.duty_cycle_speed = 6.0
        self.duty_cycle_neutral = 91.5
        self.duty_cycle_left = self.duty_cycle_neutral
        self.duty_cycle_right = self.duty_cycle_neutral
        self.duty_cycle_increment_increase = 1
        self.duty_cycle_increment_descrease = -1
        self.duty_cycle_increment_left = 0.0
        self.duty_cycle_increment_right = 0.0
        self.duty_cycle_increment = 0.65 # test percent of self.duty_cycle_speed
        self.duty_cycle_max_difference = 2
        self.encoder_ticks_left = 0
        self.encoder_ticks_right = 0
        self.encoder_ticks_left_start = 0
        self.encoder_ticks_right_start = 0

    def encoder_publisher_callback(self, msg):
        self.encoder_ticks_left = msg.left_wheel_tick_count
        self.encoder_ticks_right = msg.right_wheel_tick_count
        encoder_diff_left = abs(self.encoder_ticks_left - self.encoder_ticks_left_start)
        encoder_diff_right = abs(self.encoder_ticks_right - self.encoder_ticks_right_start)

        if abs(encoder_diff_left - encoder_diff_right) > self.duty_cycle_max_difference:
            if encoder_diff_left > encoder_diff_right:
                print('highleft')
                self.duty_cycle_increment_left = self.duty_cycle_increment * self.duty_cycle_increment_descrease
                self.duty_cycle_increment_right = self.duty_cycle_increment * self.duty_cycle_increment_increase
            else:
                print('highright')
                self.duty_cycle_increment_left = self.duty_cycle_increment * self.duty_cycle_increment_increase
                self.duty_cycle_increment_right = self.duty_cycle_increment * self.duty_cycle_increment_descrease
        else:
            print('neutral')
            self.duty_cycle_increment_left = 0.0
            self.duty_cycle_increment_right = 0.0
        
        self.duty_cycle_left = self.duty_cycle_neutral + self.motor_on_left * self.motor_direction_left * (self.duty_cycle_speed + self.duty_cycle_increment_left)
        self.duty_cycle_right = self.duty_cycle_neutral + self.motor_on_right * self.motor_direction_right * (self.duty_cycle_speed + self.duty_cycle_increment_right)

    def cmd_vel_callback(self, msg):
        self.encoder_ticks_left_start = self.encoder_ticks_left
        self.encoder_ticks_right_start = self.encoder_ticks_right

        x = msg.linear.x
        z = msg.angular.z
        if x == 0 and z == 0:
            self.motor_on_left = 0
            self.motor_on_right = 0
        elif x != 0:
            if x > 0:
                self.motor_on_left = 1
                self.motor_on_right = 1
                self.motor_direction_left = self.motor_direction_forward
                self.motor_direction_right = self.motor_direction_forward
            elif x < 0:
                self.motor_on_left = 1
                self.motor_on_right = 1
                self.motor_direction_left = self.motor_direction_backward
                self.motor_direction_right = self.motor_direction_backward
        else:
            if z > 0:
                self.motor_on_left = 1
                self.motor_on_right = 1
                self.motor_direction_left = self.motor_direction_backward
                self.motor_direction_right = self.motor_direction_forward
            else:
                self.motor_on_left = 1
                self.motor_on_right = 1
                self.motor_direction_left = self.motor_direction_forward
                self.motor_direction_right = self.motor_direction_backward

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