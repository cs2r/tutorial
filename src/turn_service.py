#!/usr/bin/env python
import rospy, time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from tutorial.srv import turn, turnResponse

class Turn():

    def __init__(self):
        rospy.init_node('Turn_with_angle')
        self.pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
        rospy.Subscriber("/turtle1/pose", Pose, self.get_theta)
        self.turn = Twist()
        self.turn.angular.z = 1.0
        self.stop = Twist()
        self.stop.angular.z = 0.0
        s = rospy.Service("/turn", turn, self.callback)
        print "service is ready"

    def callback(self, req):
        delay = req.angle
        start = time.time()
        while time.time() < start + delay:
            self.pub.publish(self.turn)
            time.sleep(0.001)
        self.pub.publish(self.stop)
        respond = turnResponse()
        respond.theta = self.theta
        return respond

    def get_theta(self, data):
        self.theta = data.theta


if __name__ == "__main__":
    move_turtle = Turn()
    rospy.spin()