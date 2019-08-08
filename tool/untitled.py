# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys,time
from ui import *

class Ui_Form(QWidget):

    state = 'init'
    thread_1 = None

    def __init__(self):
        super(Ui_Form,self).__init__()
        self.ui = ui()

    def setupUi(self):
        self.resize(583, 445)
        self.lcdNumber = QtWidgets.QLCDNumber(self)
        self.lcdNumber.setGeometry(QtCore.QRect(103, 160, 121, 61))
        self.dial = QtWidgets.QDial(self)
        self.dial.setGeometry(QtCore.QRect(260, 150, 131, 101))
        self.pushButtonStart = QtWidgets.QPushButton('开始',self)
        self.pushButtonStart.setGeometry(QtCore.QRect(100, 300, 75, 23))
        self.pushButtonReset = QtWidgets.QPushButton('重置',self)
        self.pushButtonReset.setGeometry(QtCore.QRect(300, 300, 75, 23))
        self.horizontalSlider = QtWidgets.QSlider(self)
        self.horizontalSlider.setGeometry(QtCore.QRect(100, 260, 281, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(100, 40, 311, 31))
        self.progressBar.setProperty("value", 0)
       #按钮关联
        self.dial.valueChanged['int'].connect(self.lcdNumber.display)
        self.dial.valueChanged['int'].connect(self.horizontalSlider.setValue)
        self.dial.valueChanged['int'].connect(self.progressBar.setValue)
        self.horizontalSlider.valueChanged['int'].connect(self.dial.setValue)
        self.pushButtonStart.clicked.connect(self.clickStartButton)
        self.pushButtonReset.clicked.connect(self.clickResetButton)

    def clickStartButton(self):
        '''
        点击开始按钮
        :return:
        '''
        '''
        if self.state == 'stop':
            self.pushButtonStart.setText('暂停')
            self.state = 'start'
            try:
                self.thread_1 = Work(mainUi=self)
                self.thread_1.updateValue.connect(self.updateDial)
                self.thread_1.start()
            except Exception as err:
                print(err)
        else:
            self.pushButtonStart.setText('开始')
            self.state = 'stop'
            self.thread_1.terminate()
            self.thread_1.wait()
'''
        if self.state == 'init':
            self.state = 'start'
            self.pushButtonStart.setText('暂停')
            self.thread_1 = Work(mainUi=self)
            self.thread_1.updateValue.connect(self.updateDial)
            self.thread_1.start()
        elif self.state == 'start':
            self.state = 'stop'
            self.pushButtonStart.setText('开始')
        elif self.state == 'stop':
            self.state = 'start'
            self.pushButtonStart.setText('暂停')

    def clickResetButton(self):
        '''
        点击重置按钮
        :return:
        '''
        if self.thread_1:
            self.thread_1.terminate()
            self.thread_1.wait()
        self.dial.setValue(0)
        self.pushButtonStart.setText('开始')
        self.state = 'init'

    def updateDial(self, value):
        self.dial.setValue(value)
        if value == 99:
            self.pushButtonStart.setText('开始')
            self.state = 'init'
            self.ui.setupUi()
            self.ui.show()

class Work(QThread):

    updateValue = pyqtSignal(int)

    def __init__(self, mainUi=None):
        super(Work,self).__init__()
        self.mainUi = mainUi

    def run(self):
        try:
           valueTmp = int(self.mainUi.lcdNumber.value())
           for i in range(valueTmp,100):
               time.sleep(0.1)
               while True:
                   if self.mainUi.state == 'stop':
                       print('stop')
                       time.sleep(0.01)
                   else:
                       break
               self.updateValue.emit(i)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    uiIns = Ui_Form()
    uiIns.setupUi()
    uiIns.show()
    sys.exit(app.exec())

