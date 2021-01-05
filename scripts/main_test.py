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
import random


n = 0
t = 0
flag = 0
phase = 0

class Test(QDialog):
    def __init__(self,parent=None):
        # GUI。
        super(Test, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # ROS。pubの設定。
        self.pub = rospy.Publisher('count/data',Int32,queue_size=1)
        self.pub2 = rospy.Publisher('number/times',Int32,queue_size=1)

    def slot1(self):
        self.ui.label_2.setText('easy')
        print('easyが選択されました')
        self.easy_turn()


    def slot2(self):
        self.ui.label_2.setText('hard')
        print('hardが選択されました')
        self.hard_turn()

    def plus1(self):
            n += 1
            print('player:', n)
            if n == 21:
                self.lose()
                flag = 4
            self.ui.label.setText('入力 : 1')
            if not flag == 4:
                self.cpu()

    def plus2(self):
        #flag:0 > senkou
            for i range(2):
                n += 1
                print('player:', n)
            self.ui.label.setText('入力 : 2')
            if n == 21:
                self.lose()
                flag == 4
            if not flag == 4:
                self.cpu()

    def plus3(self):
            for i range(3):
                n += 1
                print('player:', n)
            self.ui.label.setText('入力 : 3')
            if n == 21:
                self.lose()
                flag == 4
            if not flag == 4:
                self.cpu()

    def easy_turn(self):
        print('あなたは後攻です')
        print('start:', n)
        flag = 1

    def hard_turn(self):
        print('あなたは先行です')
        print('start:', n)
        print('1～3のボタンを一つ押してください')

    def Publisher(self, n):
        self.pub.publish(n)

    def Publisher2(self, t):
        self.pub2.publish(t)

    def GM(self):
        print('あなたのターンです')
        print('1～3のボタンを一つ押してください')

    def cpu(self):
        if flag == 1:#cpu senkou
            #easy
            self.random()
            for i in range(t):
                n += 1
                if n == 21:
                    self.lose1()
                    flag == 4
            self.Publisher(n)
            self.Publisher2(t)
            if not flag == 4:
                self.GM()

        if flag == 0:#cpu koukou
            #hard
            t = 4*phase-n
            for i in range(t):
                n += 1
                if n == 21:
                    self.lose1()
                    flag == 4
            phase += 1
            self.Publisher(n)
            self.Publisher2(t)
            if not flag == 4:
                self.GM()

    def random(self):
        choice = list(range(1, 4))
        w = [2,2,1]
        t = random.choices(choice, k = 1, weights = w)

    def lose(self):
        print('player lose')
        print('ウィンドウを閉じてください')

    def lose1(self):
        print('player win')
        print('ウィンドウを閉じてください')
        


if __name__ == '__main__':
    rospy.init_node('test')
    rospy.loginfo('count game started')
    print('初めに難易度を選択してください')
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())
