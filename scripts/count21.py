#! /usr/bin/env python3
# -*- coding: utf-8 -*-


# GUI。
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from gui import Ui_Dialog
# ROS。
import rospy
from std_msgs.msg import Int32
import random


n = 0
t = 0
flag = 0
phase = 1

class Test(QDialog):
    def __init__(self,parent=None):
        #GUI
        super(Test, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #pub
        self.pub = rospy.Publisher('count/data',Int32,queue_size=1)
        self.pub2 = rospy.Publisher('number/times',Int32,queue_size=1)

    def slot1(self):
        self.ui.label_2.setText('easy')
        print('easyが選択されました')
        print(' ')
        self.easy_turn()


    def slot2(self):
        self.ui.label_2.setText('hard')
        print('hardが選択されました')
        print(' ')
        self.hard_turn()

    def plus1(self):
            global n
            global flag

            n += 1
            print('player:', n)
            if n == 21:
                self.lose()
                flag = 4
            print('-------------------------------')
            self.ui.label.setText('入力 : 1')
            if not flag == 4:
                self.cpu()

    def plus2(self):
        #flag:0 > senkou
            global n
            global flag

            for i in range(2):
                n += 1
                print('player:', n)
                if n == 21:
                    self.lose()
                    flag = 4
                    break
            print('-------------------------------')
            self.ui.label.setText('入力 : 2')
            if not flag == 4:
                self.cpu()

    def plus3(self):
            global n
            global flag

            for i in range(3):
                n += 1
                print('player:', n)
                if n == 21:
                    self.lose()
                    flag = 4
                    break
            print('-------------------------------')
            self.ui.label.setText('入力 : 3')
            if not flag == 4:
                self.cpu()

    def easy_turn(self):
        global flag

        print('あなたは後攻です')
        print(' ')
        flag = 1
        self.cpu()

    def hard_turn(self):
        print('あなたは先行です')
        print('1～3のボタンを一つ押してください')
        print('start:', n)

    def Publisher(self, n):
        self.pub.publish(n)

    def Publisher2(self, t):
        self.pub2.publish(t)

    def GM(self):
        rospy.sleep(0.1)
        print('あなたのターンです')
        print('1～3のボタンを一つ押してください')

    def cpu(self):
        global n
        global phase
        global flag
        global t

        if flag == 1:#cpu senkou
            #easy
            self.random()
            for i in range(t):
                n += 1
                if n == 21:
                    self.lose1()
                    flag = 4
            self.Publisher(n)
            if flag == 4:
                pass
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
                    flag = 4
            phase += 1
            self.Publisher(n)
            self.Publisher2(t)
            if not flag == 4:
                self.GM()

    def random(self):
        global t
        t = random.randint(1,3)

    def lose(self):
        print('-------------------------------')
        print('player lose')
        print('ウィンドウを閉じてください')

    def lose1(self):
        print('player win')
        print('ウィンドウを閉じてください')
        print('-------------------------------')
        


if __name__ == '__main__':
    rospy.init_node('test')
    rospy.loginfo('count game started')
    print(' ')
    print('初めに難易度を選択してください')
    print(' ')
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())
