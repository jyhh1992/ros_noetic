#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
# std_msgs가 아님

def fun():
    rospy.init_node('simturtle_pub', anonymous=True)
    #  본인의 노드
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    #  받을 노드를 지정
    twist = Twist()

    # twist.linear.x=3.0
    twist.linear.x=0.0
    twist.linear.z=0.0
    twist.angular.x = twist.angular.y = twist.angular.z = 0.0

    speed = 0.3
    distance = 2
    meter = 0.5
    twist.linear.y = abs(speed)

    while not rospy.is_shutdown():
        time0 = rospy.Time.now().to_sec()
        current_distance = 0

        while (current_distance < distance):
            
            pub.publish(twist)
            time1 = rospy.Time.now().to_sec()
            current_distance = meter *(time1 - time0)
        twist.linear.y = 0
        pub.publish(twist)
        break

    # twist.linear.x=-5.0

    # rate = rospy.Rate(10)

    # while not rospy.is_shutdown():
    #     str = 'hello_pubilsher : %s ' % rospy.get_time()
    #     pub.publish(str)
    #     rate.sleep()
if __name__ == "__main__":
    try:
        fun()
    except rospy.ROSInterruptException: pass