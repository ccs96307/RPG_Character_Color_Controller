# -*- coding: utf-8 -*-
import sys
import base64
from io import BytesIO
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from test import Ui_MainWindow
from dropLabel import dLabel
from pic2str import arrow
from PIL import Image, ImageQt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.pressed.connect(self.button)

    def button(self):
        self.ui.label_3.setText('123')


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())