# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 571, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # player = QMediaPlayer()
        # mc = QMediaContent(QUrl.fromLocalFile("/home/johnny/PycharmProjects/Python_1st/assets/videos/mv.mp4"))
        # player.setMedia(mc)
        # player.setVolume(100)
        # videoWidget = QVideoWidget()
        # palette=QPalette()
        # palette.setBrush(QPalette.Background,Qt.black)
        # # videoWidget.setPalette(QPalette().setBrush(QPalette.Background,Qt.black))
        # player.setVideoOutput(videoWidget)
        # videoWidget.show()
        # # self.verticalLayout.addWidget(videoWidget)
        # player.play()



        self.btn_Play = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Play.setGeometry(QtCore.QRect(650, 90, 99, 27))
        self.btn_Play.setObjectName("btn_Play")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660, 200, 67, 17))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        # MainWindow.setCentralWidget(videoWidget)



        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_Play.setText(_translate("MainWindow", "Play"))
        self.label.setText(_translate("MainWindow", "TextLabel"))

