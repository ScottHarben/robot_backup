import rclpy
from rclpy.node import Node

from robot_interfaces.msg import TickCount, WheelRPM


class RPMPublisherRight(Node):

    def __init__(self):
        super().__init__('rpm_publisher_right')
        self.subscription = self.create_subscription(TickCount, 'encoder_ticks', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(WheelRPM, 'feedback_rpm_right', 10)
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.ticks_current = 0
        self.ticks_previous = 0
        self.time_current = self.get_clock().now()
        self.time_previous = self.get_clock().now()

        self.ticks_per_revolution = 696.5
        self.rpm_to_radians = 0.10471975512
        self.wheel_radius = 0.060

    def listener_callback(self, msg):
        self.ticks_current = msg.right_wheel_tick_count

    def timer_callback(self):
        self.time_current = self.get_clock().now()
                
        ticks_difference = self.ticks_current - self.ticks_previous
        if (ticks_difference < -10000):
            ticks_difference = ticks_difference + 65535
        elif(ticks_difference > 10000):
            ticks_difference = 0 - (65535 - ticks_difference)

        delta_time = (self.time_current - self.time_previous).nanoseconds / 1e9 # time in seconds

        rpm = (ticks_difference / (delta_time * self.ticks_per_revolution)) * 60.0

        self.ticks_previous = self.ticks_current
        self.time_previous = self.time_current

        msg = WheelRPM()
        msg.rpm_right = rpm
        self.publisher_.publish(msg)


def main(args=None):
    print('Publishing feedback_rpm_right...')
    rclpy.init(args=args)
    rpm_publisher_right = RPMPublisherRight()
    rclpy.spin(rpm_publisher_right)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    rpm_publisher_right.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()