# -*- coding: utf-8 -*-
import re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class dLabel(QLabel):
    def __init__(self, widget, mainWindow):
        super(dLabel, self).__init__(widget)
        self.setAcceptDrops(True)
        self.mainWindow = mainWindow
        self.switch = 0

    def dragEnterEvent(self, event):
        file_name = event.mimeData().text()
        if file_name.split('.')[-1] in ['png', 'jpg', 'jpeg']:
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        file_path = event.mimeData().text()
        file_path = re.sub('file:///', '', file_path)
        self.setPixmap(QPixmap(file_path))
        self.setScaledContents(True)
        self.mainWindow.ui.label_image_output.setPixmap(QPixmap(file_path))
        self.mainWindow.ui.label_image_output.setScaledContents(True)
        self.switch = 1

    def mousePressEvent(self, event):
        if self.switch:
            self.mainWindow.get(event.pos())
