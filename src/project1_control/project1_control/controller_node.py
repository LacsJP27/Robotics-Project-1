import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry

class Project1Controller(Node):
    def __init__(self):
        super().__init__('project1_controller')
        
        # Publishers
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Subscriptions [cite: 157, 158, 159]
        self.scan_sub = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.key_sub = self.create_subscription(Twist, '/cmd_vel_key', self.key_callback, 10)
        
        # Control Timer (e.g., 10Hz)
        self.timer = self.create_timer(0.1, self.control_loop)
        
        # Internal State
        self.latest_scan = None
        self.manual_twist = Twist()
        self.is_colliding = False
    
    def scan_callback(self, msg):
        self.latest_scan = msg
        # Approx collision detection [cite: 161, 162]
        if min(msg.ranges) < 0.25:
            self.is_colliding = True
        else:
            self.is_colliding = False
    
    def odom_callback(self, msg):
        pass # Will use for distance tracking in Phase 3 [cite: 170]

    def key_callback(self, msg):
        self.manual_twist = msg

    def control_loop(self):
        msg = Twist()
        
        # Check if we actuall have scan data yet
        # if self.is_colliding:
        #     msg.linear.x = 0.0
        #     msg.angular.z = 0.0
        #     self.get_logger().warn('COLLISION DETECTED: HALTING')

        # # PRIORITY 1: Halt on collision [cite: 22, 104]
        # if self.is_colliding:
        #     msg.linear.x = 0.0
        #     msg.angular.z = 0.0
            
        # PRIORITY 2: Keyboard commands [cite: 23, 105]
        if (self.manual_twist.linear.x != 0.0 or self.manual_twist.angular.z != 0.0):
            msg = self.manual_twist
            
        # PRIORITY 6: Drive forward [cite: 26, 109]
        else:
            msg.linear.x = 0.2 # Slow forward crawl
            
        self.cmd_pub.publish(msg)
    
def main(args=None):
    if not rclpy.ok():
        rclpy.init(args=args)
    node = Project1Controller()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, rclpy.executors.ExternalShutdownException):
        pass
    finally:
        if rclpy.ok():
            node.destroy_node()
            rclpy.shutdown()