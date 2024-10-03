#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from robot_interfaces.msg import DualEncoder
import RPi.GPIO as GPIO
import time


class MotorSubscriber(Node):

    def __init__(self):
        super().__init__('motor0')
        self.cmd_vel_subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.cmd_vel_callback,
            10)
        self.encoder_pub_subscription = self.create_subscription(
            DualEncoder,
            'encoder_pub',
            self.encoder_pub_callback,
            10)
        self.cmd_vel_subscription
        self.encoder_pub_subscription

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.enA = 17
        self.in1 = 27
        self.in2 = 22
        self.in3 = 10
        self.in4 = 9
        self.enB = 11

        GPIO.setup(self.enA, GPIO.OUT)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.in3, GPIO.OUT)
        GPIO.setup(self.in4, GPIO.OUT)
        GPIO.setup(self.enB, GPIO.OUT)

        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)

        self.pwm1 = GPIO.PWM(self.enA, 1000)
        self.pwm2 = GPIO.PWM(self.enB, 1000)
        initial_motor_speed = 75
        self.pwm1.start(initial_motor_speed)
        self.pwm2.start(initial_motor_speed)
        self.power_l = initial_motor_speed
        self.power_r = initial_motor_speed

        self.increment_motor_speed = 5

        self.left_count = 0
        self.right_count = 0
        self.prev_ticks_l = 0
        self.prev_ticks_r = 0

    def cmd_vel_callback(self, data):
        x = data.linear.x
        z = data.angular.z
        if x == 0 and z == 0:
            GPIO.output(self.in1, GPIO.LOW)
            GPIO.output(self.in2, GPIO.LOW)
            GPIO.output(self.in3, GPIO.LOW)
            GPIO.output(self.in4, GPIO.LOW)
        elif x != 0:
            if x > 0:
                GPIO.output(self.in1, GPIO.HIGH)
                GPIO.output(self.in2, GPIO.LOW)
                GPIO.output(self.in3, GPIO.HIGH)
                GPIO.output(self.in4, GPIO.LOW)
            else:
                GPIO.output(self.in1, GPIO.LOW)
                GPIO.output(self.in2, GPIO.HIGH)
                GPIO.output(self.in3, GPIO.LOW)
                GPIO.output(self.in4, GPIO.HIGH)
        else:
            if z > 0:
                GPIO.output(self.in1, GPIO.LOW)
                GPIO.output(self.in2, GPIO.HIGH)
                GPIO.output(self.in3, GPIO.HIGH)
                GPIO.output(self.in4, GPIO.LOW)
            else:
                GPIO.output(self.in1, GPIO.HIGH)
                GPIO.output(self.in2, GPIO.LOW)
                GPIO.output(self.in3, GPIO.LOW)
                GPIO.output(self.in4, GPIO.HIGH)

    def encoder_pub_callback(self, data):
        self.left_count += data.left_count
        self.right_count += data.right_count
        self.set_motor_speeds(self.left_count, self.right_count)

    def set_motor_speeds(self, num_ticks_l, num_ticks_r):
        self.prev_ticks_l
        self.prev_ticks_r
        self.power_l
        self.power_r
        diff_l = num_ticks_l - self.prev_ticks_l
        diff_r = num_ticks_r - self.prev_ticks_r
        self.prev_ticks_l = num_ticks_l
        self.prev_ticks_r = num_ticks_r
        if (diff_l > diff_r):
            self.power_l -= self.increment_motor_speed
            self.power_r += self.increment_motor_speed
        if (diff_r > diff_l):
            self.power_l += self.increment_motor_speed
            self.power_r -= self.increment_motor_speed
        if self.power_l < 10:
            self.power_l = 5
        if self.power_l > 90:
            self.power_l = 95
        if self.power_r < 10:
            self.power_r = 5
        if self.power_r > 90:
            self.power_r = 95
        self.pwm1.ChangeDutyCycle(self.power_l)
        self.pwm2.ChangeDutyCycle(self.power_r)
        time.sleep(.02)


def main(args=None):
    rclpy.init(args=args)
    motor_subscriber = MotorSubscriber()
    print("listening for motor commands")
    rclpy.spin(motor_subscriber)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
