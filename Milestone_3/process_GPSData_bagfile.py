
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseStamped

class ProcessGPSBag(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            PoseStamped,
            'GPSData',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.cnt = 0

        self.fp = open('GPSout.txt', 'w')
        print('UTM E, UTM N', file=self.fp)

    def listener_callback(self, msg):
        self.get_logger().info('cnt = "%d' % self.cnt)
        self.cnt = self.cnt + 1
        print('gps count = ', self.cnt)
        print(msg.pose.position.x, ', ', msg.pose.position.y, file = self.fp)

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = ProcessGPSBag()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()