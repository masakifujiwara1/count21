#! /usr/bin/env python3
# -*- coding: utf-8 -*-


# GUI。
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from test import Ui_Dialog
# ROS。
import rospy
from std_msgs.msg import Int32


print('初めに難易度を選択してください')
n=0

class Test(QDialog):
    def __init__(self,parent=None):
        # GUI。
        super(Test, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # ROS。pubの設定。
        self.pub = rospy.Publisher('count/data',Int32,queue_size=1)

    def slot1(self):
        self.ui.label_2.setText('easy')
        print('easyが選択されました')
        self.easy_turn()

        self.cmd_vel_Twist.angular.z = 1 # 1[rad/s]で左に回転
        self.pub_cmd_vel.publish(self.cmd_vel_Twist)
        self.cmd_vel_Twist.angular.z = 0

    def slot2(self):
        self.ui.label_2.setText('hard')
        print('hardが選択されました')
        self.hard_turn()

        self.cmd_vel_Twist.linear.x = 1 # 1[m/s]で直進
        self.pub_cmd_vel.publish(self.cmd_vel_Twist)
        self.cmd_vel_Twist.linear.x = 0

    def plus1(self):
        self.cmd_vel_Twist.angular.z = -1 # 1[rad/s]で右に回転
        self.pub_cmd_vel.publish(self.cmd_vel_Twist)
        self.cmd_vel_Twist.angular.z = 0

    def plus2(self):
        pass

    def plus3(self):
        pass

    def easy_turn(self):
        print('あなたは後攻です')

    def hard_turn(self):
        print('あなたは先行です')

    def Publisher(self, n):
        self.pub.publish(n)



if __name__ == '__main__':
    rospy.init_node('test')
    rospy.loginfo('count game started')
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())
