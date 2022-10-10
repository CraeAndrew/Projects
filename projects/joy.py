import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy

from std_msgs.msg import Int16

#from drive_interfaces.msg import VehCmd

from geometry_msgs.msg import Twist

#from .ports import ports


import array
import math


class Joy_Count(Node):

    def __init__(self):
        super().__init__('joy')
        self.subscription = self.create_subscription(
            Joy,'joy',self.listener_callback,10)
        self.subscription  # prevent unused variable warning

        #self.publisher = self.create_publisher(Int16, 'led_color', 10)

        #self.publisher2 = self.create_publisher(VehCmd, 'vehicle_command_angle', 10)


    def listener_callback(self, msg):
        
        #throttle_effort = 0.00 to 100.00 %
            # (-) throttle is reverse
        #steering_angle = -45 to 45 (degrees)
            # (-) is left , (+) is right
        
        self.get_logger().info('"%s"' % msg.axes)
        
        #self.publisher.publish(msg)
        #self.publisher2.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    joy = Joy_Count()

    rclpy.spin(joy)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    joy.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
