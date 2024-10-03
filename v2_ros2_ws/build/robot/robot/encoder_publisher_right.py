import rclpy
from rclpy.node import Node
import Jetson.GPIO as GPIO
from robot_interfaces.msg import TickCount
from geometry_msgs.msg import Twist

class EncoderPublisherRight(Node):

    def __init__(self):
        super().__init__('encoder_publisher_right')
        self.cmd_vel_subscription = self.create_subscription(Twist, 'cmd_vel', self.cmd_vel_callback, 10)
        self.cmd_vel_subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(TickCount, 'encoder_ticks_right', 10)
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.encoder_right_a = 16
        self.encoder_right_b = 18
        self.motor_direction = 0
        self.encoder_minimum = -32768
        self.encoder_maximum = 32767
        self.right_wheel_tick_count = 0

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.encoder_right_a, GPIO.IN)

        GPIO.add_event_detect(self.encoder_right_a, GPIO.RISING, callback=self.right_wheel_tick)

    def cmd_vel_callback(self, msg):
        if msg.linear.x > 0 or msg.angular.z > 0:
            self.motor_direction = 1
        elif msg.angular.z < 0:
            self.motor_direction = -1

    def right_wheel_tick(self, channel):
        self.right_wheel_tick_count += self.motor_direction 

        if self.motor_direction == 1:
            if self.right_wheel_tick_count == self.encoder_maximum:
                self.right_wheel_tick_count = self.encoder_minimum
        elif self.motor_direction == -1:
            if self.right_wheel_tick_count == self.encoder_minimum:
                self.right_wheel_tick_count = self.encoder_maximum

    def timer_callback(self):
        msg = TickCount()
        msg.right_wheel_tick_count = self.right_wheel_tick_count
        self.publisher_.publish(msg)


def main(args=None):
    print('Publishing encoder_ticks_right...')
    rclpy.init(args=args)
    encoder_publisher_right = EncoderPublisherRight()
    rclpy.spin(encoder_publisher_right)
    GPIO.cleanup()

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    encoder_publisher_right.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
