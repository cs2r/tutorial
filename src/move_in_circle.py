#!/usr/bin/env python
import rospy, time
from geometry_msgs.msg import Twist


def move():
    rospy.init_node('Move_in_circle')
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    cmd = Twist()
    cmd.linear.x = 1.0
    cmd.angular.z = 1.0
    while not rospy.is_shutdown():
        pub.publish(cmd)


if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass