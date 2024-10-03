import rclpy
from rclpy.node import Node
from robot_interfaces.msg import TowerData
import smbus
import time


class T2DistancePublisher(Node):

    def __init__(self):
        super().__init__('t2_distance_publisher')
        self.publisher_ = self.create_publisher(TowerData, 't2_dist', 10)
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.bus = smbus.SMBus(0) # Change the I2C bus number based on the actual device
        self.address = 0x10 # Radar default address 0x10
        self.getLidarDataCmd = [0x5A,0x05,0x00,0x01,0x60] # Gets the distance value instruction


    def timer_callback(self):
        self.bus.write_i2c_block_data(self.address, 0x00, self.getLidarDataCmd)
        time.sleep(0.01)
        data = self.bus.read_i2c_block_data(self.address, 0x00, 9)
        distance = data[0] | (data[1] << 8)
        msg = TowerData()
        msg.distance = distance
        self.publisher_.publish(msg)


def main(args=None):
    print('Publishing t2_dist...')
    rclpy.init(args=args)
    t2_distance_publisher = T2DistancePublisher()
    rclpy.spin(t2_distance_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    t2_distance_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
