# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1026, 648)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_image_original = QtWidgets.QLabel(self.centralwidget)
        self.label_image_original.setGeometry(QtCore.QRect(0, 30, 400, 400))
        self.label_image_original.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_image_original.setText("")
        self.label_image_original.setObjectName("label_image_original")
        self.label_text_original = QtWidgets.QLabel(self.centralwidget)
        self.label_text_original.setGeometry(QtCore.QRect(0, 0, 400, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_text_original.setFont(font)
        self.label_text_original.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_text_original.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_original.setObjectName("label_text_original")
        self.pushButton_upload = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_upload.setGeometry(QtCore.QRect(155, 430, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_upload.setFont(font)
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 480, 1091, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(780, 430, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.label_image_output = QtWidgets.QLabel(self.centralwidget)
        self.label_image_output.setGeometry(QtCore.QRect(625, 30, 400, 400))
        self.label_image_output.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_image_output.setText("")
        self.label_image_output.setObjectName("label_image_output")
        self.label_text_output = QtWidgets.QLabel(self.centralwidget)
        self.label_text_output.setGeometry(QtCore.QRect(625, 0, 400, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_text_output.setFont(font)
        self.label_text_output.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_text_output.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_output.setObjectName("label_text_output")
        self.label_color_original = QtWidgets.QLabel(self.centralwidget)
        self.label_color_original.setGeometry(QtCore.QRect(20, 520, 100, 100))
        self.label_color_original.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_color_original.setText("")
        self.label_color_original.setObjectName("label_color_original")
        self.label_arrow = QtWidgets.QLabel(self.centralwidget)
        self.label_arrow.setGeometry(QtCore.QRect(150, 520, 100, 100))
        self.label_arrow.setStyleSheet("")
        self.label_arrow.setText("")
        self.label_arrow.setObjectName("label_arrow")
        self.label_color_output = QtWidgets.QLabel(self.centralwidget)
        self.label_color_output.setGeometry(QtCore.QRect(280, 520, 100, 100))
        self.label_color_output.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_color_output.setText("")
        self.label_color_output.setObjectName("label_color_output")
        self.horizontalSlider_R = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_R.setGeometry(QtCore.QRect(440, 520, 160, 22))
        self.horizontalSlider_R.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_R.setObjectName("horizontalSlider_R")
        self.label_text_R = QtWidgets.QLabel(self.centralwidget)
        self.label_text_R.setGeometry(QtCore.QRect(410, 520, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_text_R.setFont(font)
        self.label_text_R.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_text_R.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_R.setObjectName("label_text_R")
        self.label_B = QtWidgets.QLabel(self.centralwidget)
        self.label_B.setGeometry(QtCore.QRect(410, 600, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_B.setFont(font)
        self.label_B.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_B.setAlignment(QtCore.Qt.AlignCenter)
        self.label_B.setObjectName("label_B")
        self.horizontalSlider_B = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_B.setGeometry(QtCore.QRect(440, 600, 160, 22))
        self.horizontalSlider_B.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_B.setObjectName("horizontalSlider_B")
        self.label_text_G = QtWidgets.QLabel(self.centralwidget)
        self.label_text_G.setGeometry(QtCore.QRect(410, 560, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_text_G.setFont(font)
        self.label_text_G.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_text_G.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_G.setObjectName("label_text_G")
        self.horizontalSlider_G = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_G.setGeometry(QtCore.QRect(440, 560, 160, 22))
        self.horizontalSlider_G.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_G.setObjectName("horizontalSlider_G")
        self.lineEdit_R = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_R.setGeometry(QtCore.QRect(620, 520, 51, 21))
        self.lineEdit_R.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_R.setObjectName("lineEdit_R")
        self.lineEdit_G = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_G.setGeometry(QtCore.QRect(620, 560, 51, 21))
        self.lineEdit_G.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_G.setObjectName("lineEdit_G")
        self.lineEdit_B = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_B.setGeometry(QtCore.QRect(620, 600, 51, 21))
        self.lineEdit_B.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_B.setObjectName("lineEdit_B")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(460, 30, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Character Color Controller"))
        self.label_text_original.setText(_translate("MainWindow", "Original"))
        self.pushButton_upload.setText(_translate("MainWindow", "Upload"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.label_text_output.setText(_translate("MainWindow", "Output"))
        self.label_text_R.setText(_translate("MainWindow", "R"))
        self.label_B.setText(_translate("MainWindow", "B"))
        self.label_text_G.setText(_translate("MainWindow", "G"))
        self.lineEdit_R.setText(_translate("MainWindow", "0"))
        self.lineEdit_G.setText(_translate("MainWindow", "0"))
        self.lineEdit_B.setText(_translate("MainWindow", "0"))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit"))
