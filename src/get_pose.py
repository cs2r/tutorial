#!/usr/bin/env python
import rospy, time
from turtlesim.msg import Pose

def callback(data):
    rospy.loginfo("the turtle is in position (%f, %f)", data.x, data.y)


def get_pose():
    rospy.init_node('Get_pose')
    rospy.Subscriber("/turtle1/pose", Pose, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        get_pose()
    except rospy.ROSInterruptException:
        pass