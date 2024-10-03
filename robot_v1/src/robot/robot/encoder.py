#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from robot_interfaces.msg import DualEncoder
import RPi.GPIO as GPIO


class EncoderPublisher(Node):

    def __init__(self):
        super().__init__('encoder0')
        self.publisher_ = self.create_publisher(DualEncoder, 'encoder_pub', 10)
        self.prevTickLeft = 0
        self.prevTickRight = 0
        self.timer_ = self.create_timer(0.01, self.publish_encoder)

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.left_encoder = 14
        self.right_encoder = 15
        GPIO.setup(self.left_encoder, GPIO.IN)
        GPIO.setup(self.right_encoder, GPIO.IN)

    def publish_encoder(self):
        msg = DualEncoder()
        tickLeft = GPIO.input(self.left_encoder)
        tickRight = GPIO.input(self.right_encoder)
        if tickLeft - self.prevTickLeft == 1:
            msg.left_count = tickLeft
        else:
            msg.left_count = 0
        if tickRight - self.prevTickRight == 1:
            msg.right_count = tickRight
        else:
            msg.right_count = 0
        if msg.right_count == 1 or msg.left_count == 1:
            self.publisher_.publish(msg)
        self.prevTickLeft = tickLeft
        self.prevTickRight = tickRight

def main(args=None):
    rclpy.init(args=args)
    encoder_publisher = EncoderPublisher()
    print("publishing encoder ticks")
    rclpy.spin(encoder_publisher)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
