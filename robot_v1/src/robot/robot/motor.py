#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO
import math

class Motor:
    def __init__(self, pinFwd, pinBack, pwmPin, frequency=20, maxSpeed=100):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(pinFwd, GPIO.OUT)
        GPIO.setup(pinBack, GPIO.OUT)
        GPIO.setup(pwmPin, GPIO.OUT)

        self._frequency = frequency
        self._maxSpeed = maxSpeed
        self._pinFwd = pinFwd
        self._pinBack = pinBack
        self._pwmPin = GPIO.PWM(pwmPin, frequency)
        self.stop()

    def stop (self):
        self.run(0)
    
    def run (self, speed):
        if speed > self._maxSpeed:
            speed = self._maxSpeed
        if speed < -self._maxSpeed:
            speed = -self._maxSpeed

        if speed < 0:
            GPIO.output(self._pinFwd, GPIO.LOW)
            GPIO.output(self._pinBack, GPIO.HIGH)
            self._pwmPin.start(-speed)
        else:
            GPIO.output(self._pinFwd, GPIO.HIGH)
            GPIO.output(self._pinBack, GPIO.LOW)
            self._pwmPin.start(speed)

class Wheelie(Node):
    def __init__(self, name,
                 pinRightFwd, pinRightRev, pwmRight, 
                 pinLeftFwd, pinLeftRev, pwmLeft,
                 wheel_diameter = 0.066, wheel_base = 0.025, 
                 left_max_rpm = 200.0, right_max_rpm = 200.0,
                 frequency = 20):
        
        super().__init__(name) #motor0
        self.cmd_vel_subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self._cmd_vel_callback,
            10)
        self.cmd_vel_subscription

        self._frequency = frequency
        self._left_max_rpm = left_max_rpm
        self._right_max_rpm = right_max_rpm
        self._wheel_diameter = wheel_diameter
        self._wheel_base = wheel_base
        self._rightWheel = Motor(pinRightFwd, pinRightRev, pwmRight, frequency)
        self._leftWheel = Motor(pinLeftFwd, pinLeftRev, pwmLeft, frequency)

        self.speed = 0.0
        self.spin = 0.0

    def _cmd_vel_callback(self, msg):
        self.speed = msg.linear.x
        self.spin = msg.angular.z
        self._set_motor_speeds()

    def _set_motor_speeds(self):
        right_twist_mps = self.spin * self._wheel_base / self._wheel_diameter
        left_twist_mps = -1.0 * self.spin * self._wheel_base / self._wheel_diameter
        
        right_mps = self.speed + right_twist_mps
        left_mps = self.speed + left_twist_mps
        
        right_target_rpm = (right_mps * 60.0) / (math.pi * self._wheel_diameter)
        left_target_rpm = (left_mps * 60.0) / (math.pi * self._wheel_diameter)
        
        right_percentage = (left_target_rpm / self._left_max_rpm) * 100.0
        left_percentage = (right_target_rpm / self._right_max_rpm) * 100.0
        
        right_percentage = max (min (right_percentage, 100.0), -100.0)
        left_percentage = max (min (left_percentage, 100.0), -100.0)

        self._rightWheel.run(right_percentage)
        self._leftWheel.run(left_percentage)

def main(args=None):
    rclpy.init(args=args)
    wheelie = Wheelie('motor0', 
                      pinRightFwd=27, pinRightRev=22, pwmRight=17,
                      pinLeftFwd=10, pinLeftRev=9, pwmLeft=11,
                      left_max_rpm=195, right_max_rpm=202)
    print("listening for motor commands")
    rclpy.spin(wheelie)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
