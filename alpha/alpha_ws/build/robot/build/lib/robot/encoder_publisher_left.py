import rclpy
from rclpy.node import Node
from numpy import average, round
import RPi.GPIO as GPIO
from robot_interfaces.msg import TickCount, WheelRPM


class EncoderPublisherLeft(Node):

    def __init__(self):
        super().__init__('encoder_publisher_left')
        self.publisher_ = self.create_publisher(TickCount, 'encoder_ticks_left', 10)

        self.target_rpm_subscription = self.create_subscription(WheelRPM, 'target_rpm', self.target_rpm_callback, 10)
        self.target_rpm_subscription  # prevent unused variable warning
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.encoder_a = 11
        #self.encoder_b = 13
        self.encoder_minimum = -32768
        self.encoder_maximum = 32767
        self.wheel_tick_count = 0
        self.direction_forward = True

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.encoder_a, GPIO.IN)
        #GPIO.setup(self.encoder_b, GPIO.IN)

        GPIO.add_event_detect(self.encoder_a, GPIO.RISING, callback=self.wheel_tick)

    def wheel_tick(self, channel):
        if (self.direction_forward):
            if (self.wheel_tick_count == self.encoder_maximum):
                self.wheel_tick_count = self.encoder_minimum
            else:
                self.wheel_tick_count += 1
        else:
            if (self.wheel_tick_count == self.encoder_minimum):
                self.wheel_tick_count = self.encoder_maximum
            else:
                self.wheel_tick_count -= 1

    def target_rpm_callback(self, msg):
        if (msg.rpm_left > 0):
            self.direction_forward = True
        elif (msg.rpm_left < 0):
            self.direction_forward = False


    def timer_callback(self):
        msg = TickCount()
        msg.left_wheel_tick_count = self.wheel_tick_count
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
