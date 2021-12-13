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

    speed = 40
    angle = 180

    angluar_speed = (speed*3.14*2)/360
    # 각속도
    relative = (angle*3.14*2)/360
    # 각변위 또는 각도

    twist.linear.x= twist.linear.y= twist.linear.z=0.0
    twist.angular.x = twist.angular.y = 0.0
    twist.angular.z = 3.14

    time0 = rospy.Time.now().to_sec()
    current = 0
    twist.angular.z = angluar_speed
    

    while (current<relative):
        pub.publish(twist)
        time = rospy.Time.now().to_sec()
        current = current*(time-time0)

    twist.angular.z=0.0
    pub.publish(twist)
   
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