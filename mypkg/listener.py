import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16


##rclpy.init()
##node = Node("listener")

class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.pub = self.create_publisher(Int16, "countup", 10)
        self.n = 0
        self.create_timer(0.5, self.cb)


##def cb(msg):
    ##global node
    ##node.get_logger().info("Listen: %d" % msg.data)

    def cb(self):
        self.get_logger().info("Listen: %d" % msg.data)


##def main():
    ##pub = node.create_subscription(Int16, "countup", cb, 10)
    ##rclpy.spin(node)

def main():

    rclpy.spin(node)
