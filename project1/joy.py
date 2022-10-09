import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import PointCloud

from std_msgs.msg import Int16

from geometry_msgs.msg import Point32

import array
import math


class Joy(Node):

    def __init__(self):
        super().__init__('joy')
        self.subscription = self.create_subscription(
            Int16,'Joy',self.listener_callback,10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('"%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    joy = Joy()

    rclpy.spin(joy)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    joy.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
