#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent

class Robot:
	def __init__(self):
		self.pub = rospy.Publisher('/mobile_base/commands/velocity', Twist)
		rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, self.bumped )
		self.state = "go forward"
		self.timeChanged = rospy.get_time()

	def bumped(self, msg):
		if self.state == "go forward"
			self.state = "go backward"
			self.timeChanged = rospy.get_time()

	def run(self):
		rate = rospy.Rate(10)
		twist = Twist()
		while not rospy.is_shutdown():
			if self.state == "go forward":
				twist.linear.x = 0.1
			elif self.state == "go backward":
				twist.linear.x = -0.1
				if self.timeChanged - rospy.get_time() > 2:
					self.state = "turn"
			elif self.state == "turn":
				self.timeChanged = rospy.get_time()
				twist.angular.z = 1
				if self.timeChanged - rospy.get_time() > 2:
					self.state = "go forward"
		
			self.pub.publish(twist)
			rate.sleep()
rospy.init_node('prison_break')
robot = Robot()

robot.run()
