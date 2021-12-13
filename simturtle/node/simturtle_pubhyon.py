#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    msg = Twist()


    # 방향 관련 변수 초기화
    msg.linear.y = 0
    msg.linear.y = 0
    msg.linear.z = 0
    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0


    print("Let's move your robot")
    speed = float(input("얼마나 빠르게 이동할까요?:"))
    distance = float(input("얼만큼 이동할까요?:"))
    isDirect = str(input("방향?: (f: 전진, b: 후진, l:좌측, r:우측)"))


    if(isDirect == "f"):
        msg.linear.x = abs(speed)
    elif(isDirect == "b"):
        msg.linear.x = -abs(speed)
    elif(isDirect == "l"):
        msg.linear.y = abs(speed)
    elif(isDirect == "r"):
        msg.linear.y = -abs(speed)


    while not rospy.is_shutdown():
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while(current_distance < distance):
            velocity_publisher.publish(msg)
            t1=rospy.Time.now().to_sec()
            current_distance= speed*(t1-t0)

        msg.linear.x = 0
        velocity_publisher.publish(msg)

if __name__ == '__main__':
    try: move()
    except rospy.ROSInterruptException: pass