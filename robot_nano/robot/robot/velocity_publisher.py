import rclpy
from rclpy.node import Node

from robot_interfaces.msg import TickCount, WheelVelocity


class VelocityPublisher(Node):

    def __init__(self):
        super().__init__('velocity_publisher')
        self.subscription = self.create_subscription(TickCount, 'encoder_ticks', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(WheelVelocity, 'feedback_velocity', 10)
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.left_ticks_current = 0
        self.right_ticks_current = 0
        self.left_ticks_previous = 0
        self.right_ticks_previous = 0
        self.time_current = self.get_clock().now()
        self.time_previous = self.get_clock().now()

        self.ticks_per_revolution = 696.5
        self.rpm_to_radians = 0.10471975512
        self.wheel_radius = 0.0675

    def listener_callback(self, msg):
        self.left_ticks_current = msg.left_wheel_tick_count
        self.right_ticks_current = msg.right_wheel_tick_count

    def timer_callback(self):
        self.time_current = self.get_clock().now()
        
        left_ticks_difference = self.left_ticks_current - self.left_ticks_previous
        if (left_ticks_difference < -10000):
            left_ticks_difference = left_ticks_difference + 65535
        elif(left_ticks_difference > 10000):
            left_ticks_difference = 0 - (65535 - left_ticks_difference)
                
        right_ticks_difference = self.right_ticks_current - self.right_ticks_previous
        if (right_ticks_difference < -10000):
            right_ticks_difference = right_ticks_difference + 65535
        elif(right_ticks_difference > 10000):
            right_ticks_difference = 0 - (65535 - right_ticks_difference)

        delta_time = (self.time_current - self.time_previous).nanoseconds / 1e9 # time in seconds
        adjusted_rpm_time = 60.0 / delta_time # callback time may not be exactly 0.1 seconds

        left_wheel_rpm = left_ticks_difference * adjusted_rpm_time / self.ticks_per_revolution
        right_wheel_rpm = right_ticks_difference * adjusted_rpm_time / self.ticks_per_revolution
        angular_velocity_left = left_wheel_rpm * self.rpm_to_radians
        angular_velocity_right = right_wheel_rpm * self.rpm_to_radians
        linear_velocity_left = self.wheel_radius * angular_velocity_left
        linear_velocity_right = self.wheel_radius * angular_velocity_right

        self.left_ticks_previous = self.left_ticks_current
        self.right_ticks_previous = self.right_ticks_current
        self.time_previous = self.time_current

        msg = WheelVelocity()
        msg.linear_velocity_left = linear_velocity_left
        msg.linear_velocity_right = linear_velocity_right
        self.publisher_.publish(msg)


def main(args=None):
    print('Publishing feedback_velocity...')
    rclpy.init(args=args)
    velocity_publisher = VelocityPublisher()
    rclpy.spin(velocity_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    velocity_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()