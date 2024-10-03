import rclpy
from rclpy.node import Node
from robot_interfaces.msg import RobotPose, TowerData
import numpy as np

class RobotPosePublisher(Node):

    def __init__(self):
        super().__init__('robot_pose_publisher')
        self.t1_tower_data_subscription = self.create_subscription(TowerData, 't1_tower_data', self.t1_tower_data_callback, 10)
        self.t1_tower_data_subscription  # prevent unused variable warning
        self.t2_tower_data_subscription = self.create_subscription(TowerData, 't2_tower_data', self.t2_tower_data_callback, 10)
        self.t2_tower_data_subscription  # prevent unused variable warning
        
        self.publisher_ = self.create_publisher(RobotPose, 'robot_pose', 10)
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        # distance in m
        self.t1_dist = 0.0
        self.t1_target_aquired = False
        self.t1_heading = 0.0
        self.t2_dist = 0.0
        self.t2_target_aquired = False
        self.t2_heading = 0.0
        self.t2_offset = 19.2
        self.q1_is_heading = True
        self.x = 0.0
        self.y = 0.0
        self.heading = 0.0

    def t1_tower_data_callback(self, msg):
        if msg.qr_id == 1:
            self.q1_is_heading = True
        else:
            self.q1_is_heading = False
        self.t1_dist = float(msg.distance)
        servo_heading = float(msg.heading) - 4.0 # physical servo is offline
        self.t1_heading = np.interp(servo_heading, [0, 180], [30, 330])
        self.t1_target_aquired = msg.target_aquired

    def t2_tower_data_callback(self, msg):
        self.t2_dist = float(msg.distance)
        servo_heading = float(msg.heading) - 7.0 # physical servo is offline
        self.t2_heading = np.interp(servo_heading, [0, 180], [30, 330])
        self.t2_target_aquired = msg.target_aquired

    def timer_callback(self):
        t2_heading_supp = 180.0 - abs(t2_heading)
        t2_offset_dist = np.sqrt(np.square(self.t2_offset) + np.square(self.t2_dist) - 2 * self.t2_offset * self.t2_dist * np.cos(np.deg2rad(t2_heading_supp)))
        t2_offset_angle = np.rad2deg(np.arcsin(self.t2_dist * np.sin(np.deg2rad(t2_heading_supp)) / t2_offset_dist))
        t2_offset_angle_rel = t2_offset_angle * (self.t2_heading / abs(self.t2_heading))
        t2_offset_supp = 180.0 - t2_offset_angle
        
        x_side_value = self.t1_heading - t2_offset_angle_rel
        x_side = x_side_value / abs(x_side_value)
        
        q_angle = 360.0 - (180.0 + t2_offset_angle_rel + self.t1_heading)
        if x_side == 1:
            q_angle = q_angle - 360.0
        q_angle = abs(q_angle)
        q_dist = np.sqrt(np.square(self.t1_dist) + np.square(t2_offset_dist) - 2 * self.t1_dist * t2_offset_dist * np.cos(np.deg2rad(q_angle)))
        q1_angle = np.rad2deg(np.arcsin(t2_offset_dist * np.sin(np.deg2rad(q_angle)) / q_dist))
        q1_comp = 90.0 - q1_angle
        
        t1_x_angle = 90.0 - q1_comp
        t1_x = np.sin(np.deg2rad(t1_x_angle)) * self.t1_dist
        t1_y = np.sqrt(np.square(self.t1_dist) - np.square(t1_x))
        
        self.x = t1_x * x_side
        self.y = t1_y - q_dist / 2
        if self.q1_is_heading:
            self.heading = 180.0 - (t1_x_angle * x_side) + self.t1_heading
        else:
            self.heading = 360.0 - (t1_x_angle * x_side) + self.t1_heading
            
        msg = RobotPose()
        msg.x = self.x
        msg.y = self.y
        msg.heading = self.heading
        self.publisher_.publish(msg)


def main(args=None):
    print('Publishing robot_pose...')
    rclpy.init(args=args)
    robot_pose_publisher = RobotPosePublisher()
    rclpy.spin(robot_pose_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    robot_pose_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
