import rclpy
from rclpy.node import Node
from robot_interfaces.msg import TowerData
from threading import Thread
from pyzbar.pyzbar import decode
import cv2
import numpy as np

def gstreamer_pipeline(
    sensor_id=0,
    capture_width=1920,
    capture_height=1080,
    display_width=960,
    display_height=540,
    framerate=30,
    flip_method=0,
    ):
    return (
        "nvarguscamerasrc sensor-id=%d ! "
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

class T2DirectionPublisher(Node):

    def __init__(self):
        super().__init__('t2_direction_publisher')
        self.t2_dist_subscription = self.create_subscription(TowerData, 't2_dist', self.t2_dist_callback, 10)
        self.t2_dist_subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(TowerData, 't2_camera_direction', 10)
        
        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.vs = WebcamVideoStream().start()

        self.stop = 0.0
        self.move_left = 1.0
        self.move_right = -1.0
        self.camera_direction = self.stop

        self.frame_width = 1080
        self.frame_center = self.frame_width / 2
        self.detect_deviation_min = 0.3 # percent - prevent false detections
        self.detect_deviation_max = 3.0 # percent - prevent false detections
        self.detect_deviation = self.detect_deviation_min
        self.target_width_min = 100 # pixels
        self.target_width_max = 200 # pixels
        self.target_width = self.target_width_min
        
        self.x_center = 0
        self.x_center_prev = 0
        self.y_center_prev = 0
        self.x_percent = 0.0

        self.distance = 0
        self.qr_detected = False
        self.qr_id = 0

    def t2_dist_callback(self, msg):
        self.distance = msg.distance

    def timer_callback(self):
        frame = self.vs.read()
        qr = decode(frame)
        if len(qr) == 1:
            self.qr_detected = True
            rect = qr[0].rect
            qr_id = qr[0].data.decode('utf-8')
            if qr_id == '1' or qr_id == '2':
                self.qr_detected = True
                self.qr_id = int(qr_id)
            self.x_percent = rect.width / self.frame_width
            self.x_center = int(rect.left + (rect.width / 2))
            yCenter = int(rect.top + (rect.height / 2))

            if self.x_center_prev != 0:
                if self.x_center > self.x_center_prev + (self.x_center_prev * self.detect_deviation):
                    self.camera_direction = self.stop
                elif self.x_center < self.x_center_prev - (self.x_center_prev * self.detect_deviation):
                    self.camera_direction = self.stop
                elif yCenter > self.y_center_prev + (self.y_center_prev * self.detect_deviation):
                    self.camera_direction = self.stop
                elif yCenter < self.y_center_prev - (self.y_center_prev * self.detect_deviation):
                    self.camera_direction = self.stop
                else:
                    self.set_camera_direction()
            else:
                self.set_camera_direction()

            self.x_center_prev = self.x_center
            self.y_center_prev = yCenter
        else:
            self.qr_detected = False
            self.qr_id = 0
            self.camera_direction = self.stop

        msg = TowerData()
        msg.camera_direction = int(self.camera_direction)
        msg.distance = self.distance
        msg.qr_detected = self.qr_detected
        msg.qr_id = self.qr_id
        self.publisher_.publish(msg)

    def set_camera_direction(self):
        # the qr code gets to about 50% of the frame width at it's closest point - cap at 0.5
        # the further the qr cade is from the camera (smaller percent), the higher the detect_deviation since small movements will cause larger differences) 
        x_percent_capped = max(min(self.x_percent, 0.3), 0.05)
        self.detect_deviation = np.interp(x_percent_capped, [0.05, 0.3], [self.detect_deviation_max, self.detect_deviation_min])

        # the further the qr cade is to the camera (lower percent), the smaller the target_width since small movements will cause larger differences) 
        self.target_width = np.interp(x_percent_capped, [0.05, 0.3], [self.target_width_min, self.target_width_max])

        if self.x_center > self.frame_center + self.target_width / 2:
            self.camera_direction = self.move_left
        elif self.x_center < self.frame_center - self.target_width / 2:
            self.camera_direction = self.move_right
        else:
            self.camera_direction = self.stop


class WebcamVideoStream:
  def __init__(self, src=0):
    # initialize the video camera stream and read the first frame
    # from the stream
    self.stream = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
    (self.grabbed, self.frame) = self.stream.read()
    # initialize the variable used to indicate if the thread should
    # be stopped
    self.stopped = False

  def start(self):
    # start the thread to read frames from the video stream
    Thread(target=self.update, args=()).start()
    return self

  def update(self):
    # keep looping infinitely until the thread is stopped
    while True:
      # if the thread indicator variable is set, stop the thread
      if self.stopped:
        return
      # otherwise, read the next frame from the stream
      (self.grabbed, self.frame) = self.stream.read()

  def read(self):
    # return the frame most recently read
    return self.frame

  def stop(self):
    # indicate that the thread should be stopped
    self.stopped = True
    self.stream.release()

def main(args=None):
    print('Publishing t2_camera_direction...')
    rclpy.init(args=args)
    t2_direction_publisher = T2DirectionPublisher()
    try:
        rclpy.spin(t2_direction_publisher)
    except KeyboardInterrupt:
        t2_direction_publisher.vs.stop()
        print('USER STOPPED')
    except Exception as e:
        t2_direction_publisher.vs.stop()
        print('ERROR')
        print(e)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    t2_direction_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
