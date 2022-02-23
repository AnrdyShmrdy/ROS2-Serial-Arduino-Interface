# Node to publish a string topic
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
#TODO: Create a launch file for this Node
class SerialController(Node):
	def __init__(self):
		super().__init__('serial_controller')
		self.declare_parameter('device', '/dev/ttyACM0') #TODO: Define and set this in a .yaml config file + launch file
		self.declare_parameter('topic', 'led_state') #TODO: Define and set this in a .yaml config file + launch file
		#Example of Potential robot command: self.declare_paramter('turnLeft', 'leftMotorRoutine') 
		
  		#TODO: Change below line to fetch the parameter value from a namespace in a .yaml config file
		self.ser = serial.Serial(self.get_parameter('device').get_parameter_value().string_value,
                           9600, #Note: Baud Rate must be the same in the arduino program, otherwise signal is not recieved!
                           timeout=4)
		
  		#TODO: Change below subscription to fetch the parameter value from a namespace in a .yaml config file
		self.subscriber = self.create_subscription(String, 
                                              self.get_parameter('topic').get_parameter_value().string_value, 
                                              self.serial_listener_callback, 
                                              10)
		self.subscriber # prevent unused variable warning
	
	def serial_listener_callback(self, msg):
		#TODO: Change this so that commands are derived from a variable array of paramters. 
  		#TODO: Make it so that we can avoid editing this function in the future by editing the paramater values
		if msg.data == "on": #TODO: future format ideally would be "if msg.data == command_paramater"
			self.ser.write(b'ledon!') #TODO: future format ideally would be "if msg.data == command_value"
			self.get_logger().info('led on command sent') #TODO: "command_name" sent
		if msg.data == "off": #TODO: future format ideally would be "if msg.data == command_value"
			self.ser.write(b'ledoff!')  #TODO: future format ideally would be "if msg.data == command_value"
			self.get_logger().info('led off command sent')  #TODO: "command_name" sent


def main(args=None):
	rclpy.init(args=args)
	serial_controller = SerialController()
	rclpy.spin(serial_controller)

if __name__ == '__main__':
	main()