import rclpy
from rclpy.node import Node
import Jetson.GPIO as GPIO
from .PCA9685 import PCA9685
from robot_interfaces.msg import DutyCycle


class MotorDriver(Node):

    def __init__(self):
        super().__init__('motor_driver')
        self.subscription = self.create_subscription(DutyCycle, 'duty_cycle', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

        self.pwm_pin_left = 1
        self.pwm_pin_right = 0

        self.pwm = PCA9685()
        self.pwm.setPWMFreq(50)

        # #TODO:
        # #stop if no message recieved

    def listener_callback(self, msg):
        self.pwm.setRotationAngle(self.pwm_pin_left, msg.duty_cycle_left)
        self.pwm.setRotationAngle(self.pwm_pin_right, msg.duty_cycle_right)

def main(args=None):
    print('Running motor driver...')
    rclpy.init(args=args)
    motor_driver = MotorDriver()
    rclpy.spin(motor_driver)
    motor_driver.pwm_left.close()
    motor_driver.pwm_right.close()
    motor_driver.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()