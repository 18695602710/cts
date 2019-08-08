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

class ui(QWidget):

    def setupUi(self):
        self.resize(200, 100)
        self.pushButtonSure = QtWidgets.QPushButton('确定',self)
        self.pushButtonSure.setGeometry(QtCore.QRect(80, 50, 40, 20))
        self.label = QtWidgets.QLabel('执行完成！', self)
        self.pushButtonSure.setGeometry(QtCore.QRect(50, 10, 100, 30))
       #按钮关联
        self.pushButtonSure.clicked.connect(self.close)


