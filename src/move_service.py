#!/usr/bin/env python
import rospy, time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from tutorial.srv import move, moveResponse

class Move():

    def __init__(self):
        rospy.init_node('Move_forward')
        self.pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
        rospy.Subscriber("/turtle1/pose", Pose, self.get_pose)
        self.move = Twist()
        self.move.linear.x = 1.0
        self.stop = Twist()
        self.stop.linear.x = 0.0
        s = rospy.Service("/move_forward", move, self.callback)
        print "service is ready"

    def callback(self, req):
        delay = req.dist
        start = time.time()
        while time.time() < start + delay:
            self.pub.publish(self.move)
            time.sleep(0.001)
        self.pub.publish(self.stop)
        respond = moveResponse()
        respond.x = self.pose_x
        respond.y = self.pose_y
        return respond

    def get_pose(self, data):
        self.pose_x = data.x
        self.pose_y = data.y


if __name__ == "__main__":
    move_turtle = Move()
    rospy.spin()