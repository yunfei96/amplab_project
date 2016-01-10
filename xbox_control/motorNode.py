#!/usr/bin/python
# Put the description of your file here
# Author: Your Name <theoloong@vt.edu>
from control_motor import moveLeft
from control_motor import moveRight


# Import the Default ROS tools
import rospy
# Import the JointState message from sensor_msgs
from sensor_msgs.msg import Joy
# Import String as well
from std_msgs.msg import String


# Create variable so we can always see/use it, but set it to a value that indicates it's not yet valid
def rightMotor(msg):	
	moveRight(msg.axes[1]*100)
def leftMotor(msg):
	moveLeft(msg.axes[3]*100)

# If this is loaded as the main python file, execute the main details
if __name__ == '__main__':
  try:
    #Initialize node
    rospy.init_node('sabertooth')
    #Create publisher, to send out a String with the first joint name of every received message as an example.
    rospy.Subscriber('/joy', Joy, rightMotor)
    #Create subscriber, and tell it to call js_call() whenever a message is received
    rospy.Subscriber('/joy', Joy, leftMotor)

    #We need to wait for new messages
    rospy.spin()
  #If we are interrupted, catch the exception, but do nothing
  except rospy.ROSInterruptException:
    pass
