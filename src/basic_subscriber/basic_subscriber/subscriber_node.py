# Node to publish a string topic
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalSubscriber(Node):

	def __init__(self):
		super().__init__('minimal_subscriber')
		self.gen_led_sub = self.create_subscription(String,
			                                         'gen_led_topic',
			                                         self.listener_callback,
			                                         10)
		self.led_sub # prevent unused variable warning

	def listener_callback(self, msg):		
		self.get_logger().info('I heard: {}'.format(msg.data))

def main(args=None):
	rclpy.init(args=args)
	minimal_subscriber = MinimalSubscriber()
	rclpy.spin(minimal_subscriber)

if __name__ == '__main__':
	main()