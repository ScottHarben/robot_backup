import rclpy
from rclpy.node import Node
import pigpio

from robot_interfaces.msg import DutyCycle


class MotorDriver(Node):

    def __init__(self):
        super().__init__('motor_driver')
        self.duty_cycle_left_subscription = self.create_subscription(DutyCycle, 'duty_cycle_left', self.duty_cycle_left_callback, 10)
        self.duty_cycle_left_subscription  # prevent unused variable warning

        self.duty_cycle_right_subscription = self.create_subscription(DutyCycle, 'duty_cycle_right', self.duty_cycle_right_callback, 10)
        self.duty_cycle_right_subscription  # prevent unused variable warning

        self.pwm_pin_left = 18
        self.pwm_pin_right = 19

        self.pi = pigpio.pi()
        self.pi.exceptions = True
        #left
        self.pi.set_mode(self.pwm_pin_left, pigpio.OUTPUT)
        self.pi.set_PWM_frequency(self.pwm_pin_left, 100)
        self.pi.set_PWM_range(self.pwm_pin_left, 2000)
        self.pi.set_PWM_dutycycle(self.pwm_pin_left, 0)
        #right
        self.pi.set_mode(self.pwm_pin_right, pigpio.OUTPUT)
        self.pi.set_PWM_frequency(self.pwm_pin_right, 100)
        self.pi.set_PWM_range(self.pwm_pin_right, 2000)
        self.pi.set_PWM_dutycycle(self.pwm_pin_right, 0)

        # #TODO:
        # #stop if no message recieved

    def duty_cycle_left_callback(self, msg):
        self.pi.set_PWM_dutycycle(self.pwm_pin_left, msg.duty_cycle_left)

    def duty_cycle_right_callback(self, msg):
        self.pi.set_PWM_dutycycle(self.pwm_pin_right, msg.duty_cycle_right)

def main(args=None):
    print('Running motor driver...')
    rclpy.init(args=args)
    motor_driver = MotorDriver()
    rclpy.spin(motor_driver)
    pi.stop()
    motor_driver.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()