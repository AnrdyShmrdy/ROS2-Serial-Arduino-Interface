# Node to publish a string topic
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisher(Node):

	def __init__(self):
		super().__init__('minimal_publisher')
		self.gen_led_publisher_ = self.create_publisher(String, 'gen_led_topic', 10)
		timer_period = 3 # second
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.i = 0

	def timer_callback(self):

		gen_led = String()
		motor = String()
		if self.i % 11 == 0:
			gen_led.data = "on"
		elif self.i % 7 == 0:
			gen_led.data = "off"
		elif self.i % 5 == 0:
			gen_led.data = "off"
		elif self.i % 3 == 0:
			gen_led.data = "off"

		self.gen_led_publisher_.publish(gen_led)
		self.get_logger().info('Gen_Led data: {}'.format(gen_led.data))
		self.i += 1

def main(args=None):
	rclpy.init(args=args)
	minimal_publisher = MinimalPublisher()
	rclpy.spin(minimal_publisher)

if __name__ == '__main__':
	main()