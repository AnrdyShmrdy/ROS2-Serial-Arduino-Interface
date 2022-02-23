# Node to publish a string topic
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SerialSubscriber(Node):

	def __init__(self):
		super().__init__('serial_subscriber')
		self.declare_parameter('topic', 'led_state') #TODO: Define and set this in a .yaml config file + launch file
		#TODO: Change below line to fetch the parameter value from a namespace in a .yaml config file
		self.subscriber = self.create_subscription(String,
			                                         self.get_parameter('topic').get_parameter_value().string_value,
			                                         self.listener_callback,
			                                         10)
		self.subscriber # prevent unused variable warning

	def listener_callback(self, msg):		
		self.get_logger().info('I heard: {}'.format(msg.data))

def main(args=None):
	rclpy.init(args=args)
	serial_subscriber = SerialSubscriber()
	rclpy.spin(serial_subscriber)

if __name__ == '__main__':
	main()