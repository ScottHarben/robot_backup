import rclpy
from rclpy.node import Node
import Jetson.GPIO as GPIO
from robot_interfaces.msg import TickCount
from geometry_msgs.msg import Twist

class EncoderPublisherLeft(Node):

    def __init__(self):
        super().__init__('encoder_publisher_left')
        self.cmd_vel_subscription = self.create_subscription(Twist, 'cmd_vel', self.cmd_vel_callback, 10)
        self.cmd_vel_subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(TickCount, 'encoder_ticks_left', 10)
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.encoder_left_a = 11
        self.encoder_left_b = 13
        self.motor_direction = 0
        self.encoder_minimum = -32768
        self.encoder_maximum = 32767
        self.left_wheel_tick_count = 0

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.encoder_left_a, GPIO.IN)

        GPIO.add_event_detect(self.encoder_left_a, GPIO.RISING, callback=self.left_wheel_tick)
    
    def cmd_vel_callback(self, msg):
        if msg.linear.x > 0 or msg.angular.z < 0:
            self.motor_direction = 1
        elif msg.angular.z > 0:
            self.motor_direction = -1

    def left_wheel_tick(self, channel):
        self.left_wheel_tick_count += self.motor_direction 

        if self.motor_direction == 1:
            if self.left_wheel_tick_count == self.encoder_maximum:
                self.left_wheel_tick_count = self.encoder_minimum
        elif self.motor_direction == -1:
            if self.left_wheel_tick_count == self.encoder_minimum:
                self.left_wheel_tick_count = self.encoder_maximum

    def timer_callback(self):
        msg = TickCount()
        msg.left_wheel_tick_count = self.left_wheel_tick_count
        self.publisher_.publish(msg)


def main(args=None):
    print('Publishing encoder_ticks_left...')
    rclpy.init(args=args)
    encoder_publisher_left = EncoderPublisherLeft()
    rclpy.spin(encoder_publisher_left)
    GPIO.cleanup()

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    encoder_publisher_left.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
