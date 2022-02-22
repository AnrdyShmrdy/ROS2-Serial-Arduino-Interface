# Node to publish a string topic
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class LedController(Node):

	def __init__(self):
		super().__init__('led_controller')
#		self.declare_parameters(
#    		namespace='',
#    		parameters=[
#        		('device', "/dev/ttyACM0"),
#        		('topic', 'gen_led_topic'),
#        		('msg_data', "on"),
#				('command', b'genon!')
#    		]
#		)
#		self.ser = serial.Serial(self.get_parameter('device'))
		self.gen_led_sub = self.create_subscription(String, 'gen_led_topic', self.gen_listener_callback, 10)
		self.gen_led_sub # prevent unused variable warning
	
	def gen_listener_callback(self, msg):
		if msg.data == "on":
#			self.ser.write(self.get_parameter('command'))
#			self.ser.write(b'genon!')
#			self.get_logger().info('command in parameter sent')
			self.get_logger().info('gen on command sent')
		if msg.data == "off":
#			self.ser.write(b'genoff!')
			self.get_logger().info('gen off command sent')


def main(args=None):
	rclpy.init(args=args)
	led_controller = LedController()
	rclpy.spin(led_controller)

if __name__ == '__main__':
	main()