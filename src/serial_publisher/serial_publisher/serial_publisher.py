# Node to publish a string topic
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SerialPublisher(Node):

	def __init__(self):
		super().__init__('serial_publisher')
		self.led_state = String()
#		TODO: Have topic name grabbed from namespace in .yaml config file
		self.declare_parameter('topic', 'led_state') #TODO: Define and set this in a .yaml config file + launch file
		#TODO: Change publisher to fetch the parameter value from a namespace in a .yaml config file
		self.publisher = self.create_publisher(String, 
                                         self.get_parameter('topic').get_parameter_value().string_value, 
                                        10)
		timer_period = 0.01 # second
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.i = 0

	def timer_callback(self):
		if self.i % 2 == 0:
			self.led_state.data = "on"
		else:
			self.led_state.data = "off"
		self.publisher.publish(self.led_state)
		self.get_logger().info('Led State: {}'.format(self.led_state.data))
		self.i += 1

def main(args=None):
	rclpy.init(args=args)
	serial_publisher = SerialPublisher()
	rclpy.spin(serial_publisher)

if __name__ == '__main__':
	main()