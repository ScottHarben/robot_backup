import rclpy
from math import pi
from rclpy.node import Node
from geometry_msgs.msg import Twist
from robot_interfaces.msg import TowerData
from .PCA9685 import PCA9685
import time
import numpy as np


class T2ServoController(Node):

    def __init__(self):
        super().__init__('t2_servo_controller')
        self.t2_camera_direction_subscription = self.create_subscription(TowerData, 't2_camera_direction', self.t2_camera_direction_callback, 10)
        self.t2_camera_direction_subscription  # prevent unused variable warning
        self.t1_tower_data_subscription = self.create_subscription(TowerData, 't1_tower_data', self.t1_tower_data_callback, 10)
        self.t1_tower_data_subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(TowerData, 't2_tower_data', 10)
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.servo_pin = 15
        self.servo_min = 17
        self.servo_max = 177
        self.heading = 97
        self.qr_detected = True # set to True here to trigger the no_detection_timer
        self.qr_id = 0
        self.no_detection_time_start = self.get_clock().now()
        self.change_qr = False # if t1_change_qr, then True
        self.t2_change_qr_notification = False
        self.scanning = False
        self.scan_direction = 1
        self.target_aquired = False
        self.distance = 0
        self.pwm = PCA9685()
        self.pwm.setPWMFreq(50)

        # TODO: stop scanning after n number of full passes and put out warning message
        # TODO: qr code info (1 vs 2)
        # TODO: add logging info

    def t1_tower_data_callback(self, msg):
        if msg.change_qr_notification == True or (msg.target_aquired == True and msg.qr_id == self.qr_id):
            self.change_qr = True

    # set t2_camera_direction publish rate to change servo speed
    def t2_camera_direction_callback(self, msg):
        self.distance = msg.distance
        self.change_qr_notification = False

        if msg.qr_detected == True:
            if self.change_qr == True and msg.qr_id == self.qr_id:
                pass
            else:
                self.qr_detected = True
                self.qr_id = msg.qr_id
                self.change_qr = False
                self.scanning = False
                if msg.camera_direction == 0:
                    self.target_aquired = True
                else:
                    self.target_aquired = False
                    target_heading = self.heading + msg.camera_direction
                    if target_heading == self.servo_min - 1 or target_heading == self.servo_max + 1:
                        self.change_qr_notification = True
                        self.change_qr = True
                    else:
                        for i in np.linspace(self.heading, target_heading, 11): 
                            self.pwm.setRotationAngle(self.servo_pin, i)   
                            time.sleep(0.0175)
                        self.heading = target_heading
        elif self.qr_detected == True:
            self.qr_detected = False
            self.no_detection_time_start = self.get_clock().now()
            
        if (self.change_qr == True or
                (self.qr_detected == False and (self.get_clock().now() - self.no_detection_time_start).nanoseconds / 1e9 > 5)): # time in seconds
            self.scanning = True
            self.target_aquired = False
            if self.heading == self.servo_min:
                self.scan_direction = 1
            elif self.heading == self.servo_max:
                self.scan_direction = -1
            target_heading = self.heading + self.scan_direction
            for i in np.linspace(self.heading, target_heading, 11): 
                self.pwm.setRotationAngle(self.servo_pin, i)   
                time.sleep(0.0175)
            self.heading = target_heading

            
    def timer_callback(self):
        msg = TowerData()
        msg.distance = self.distance
        msg.heading = self.heading
        msg.change_qr = self.change_qr
        msg.target_aquired = self.target_aquired
        msg.qr_id = self.qr_id
        self.publisher_.publish(msg)

        #if this was True, make sure to set it back to False so the other tower doesn't keep trying to change
        self.change_qr_notification = False


def main(args=None):
    print('Publishing t2_tower_data...')
    rclpy.init(args=args)
    t2_servo_controller = T2ServoController()
    rclpy.spin(t2_servo_controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    t2_servo_controller.destroy_node()
    pwm.exit_PCA9685()
    rclpy.shutdown()


if __name__ == '__main__':
    main()