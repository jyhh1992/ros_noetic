#! /usr/bin/env python3

import rospy
from std_msgs.msg import String

def fun():
    return

def fun_callback(msg):
    rospy.loginfo("%s",msg.data)

    return

if __name__ == "__main__":
    rospy.init_node('sample_pubsub')
    pub = rospy.Publisher('hello', String, queue_size=10)
    rospy.Subscriber('hello02',String,callback=fun_callback)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        str = 'hello_pubilsher : %s ' % rospy.get_time()
        pub.publish(str)
        rate.sleep()

    pass