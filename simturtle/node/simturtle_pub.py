#! usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
def fun_callback(msg):
    pass
if __name__=='__main__':
    rospy.init_node('simturtle_publisher',anonymous=False)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    msg = Twist()
    velocity = 2.0
    current_velocity = 0.0
    time= 1
    rate = rospy.Rate(5)
    while current_velocity < velocity:
        msg.linear.x += 0.1
        pub.publish(msg)
        current_velocity += 0.1
        print(current_velocity)
        print(msg.linear.x)
        rate.sleep()
    pass