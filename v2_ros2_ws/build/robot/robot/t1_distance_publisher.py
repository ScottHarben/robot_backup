import rclpy
from rclpy.node import Node
from robot_interfaces.msg import TowerData
import serial
import time


class T1DistancePublisher(Node):

    def __init__(self):
        super().__init__('t1_distance_publisher')
        self.publisher_ = self.create_publisher(TowerData, 't1_dist', 10)
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.ser = serial.Serial("/dev/ttyTHS1", 115200)


    def timer_callback(self):
        counter = self.ser.in_waiting # count the number of bytes of the serial port
        if counter > 8:
            bytes_serial = self.ser.read(9)
            self.ser.reset_input_buffer()
            
            if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59: # python3
                distance = bytes_serial[2] + bytes_serial[3]*256
                self.ser.reset_input_buffer()
                msg = TowerData()
                msg.distance = distance
                self.publisher_.publish(msg)


def main(args=None):
    print('Publishing t1_dist...')
    rclpy.init(args=args)
    t1_distance_publisher = T1DistancePublisher()
    rclpy.spin(t1_distance_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    t1_distance_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
