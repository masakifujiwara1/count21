#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0
t = 0

def cb(message):
    global n
    n = message.data
    
def cb2(message):
    global n
    global t
    
    rospy.sleep(0.1)

    t = message.data
    if not n == 0:
        n -= t

    else:
        pass

    for i in range(t):
        n += 1
        print('cpu:', n)
        if n == 21:
            print('cpu lose')
            break
    print('----------------')





rospy.init_node('cpu')
rospy.loginfo('cpu log started')
sub = rospy.Subscriber('count/data', Int32, cb)
sub1 = rospy.Subscriber('number/times', Int32, cb2)
rate = rospy.Rate(60)
while not rospy.is_shutdown():
    rate.sleep()
