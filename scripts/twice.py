#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0
t = 0


def cb(message):
    global n
    n = message.data
    
def cb2(message):
    global t
    t = message.data
    n -= t

    for i range(t):
        n += 1
        print('cpu:', n)





rospy.init_node('cpu')
sub = rospy.Subscriber('count/data', Int32, cb)
sub1 = rospy.Subscriber('number/times', Int32, cb2)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    rate.sleep()
