#!/usr/bin/env python
import rospy
from tutorial.srv import move, moveRequest

def Move():
    rospy.init_node("Move_forward_client")
    rospy.wait_for_service("/move_forward")
    print "service found"
    call_service = rospy.ServiceProxy("/move_forward", move)
    print "connected to service"
    req = moveRequest()
    req.dist = 2.5
    result = call_service(req)
    print result


if __name__ == "__main__":
    service_client = Move()