
import rclpy
from rclpy.node import Node

from nav_msgs.msg import Odometry

class ProcessOdomBag(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Odometry,
            'odometry',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.cnt = 0

        self.fp = open('odom_out.txt', 'w')
        print('orient w, orient x, orient y, orient z', file=self.fp)

    def listener_callback(self, msg):
        self.get_logger().info('cnt = "%d' % self.cnt)
        self.cnt = self.cnt + 1
        print(msg.pose.pose.orientation.w, ', ', msg.pose.pose.orientation.x,  ', ', msg.pose.pose.orientation.y,  ', ', msg.pose.pose.orientation.z, file = self.fp)

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = ProcessOdomBag()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()