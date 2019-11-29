# -*- coding: utf-8 -*-
import re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PIL import Image


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
        image = Image.open(file_path)
        image = image.resize((self.size().width(), self.size().height()))

        if image.mode == "RGB":
            r, g, b = image.split()
            image = Image.merge("RGB", (b, g, r))
        elif image.mode == "RGBA":
            r, g, b, a = image.split()
            image = Image.merge("RGBA", (b, g, r, a))
        elif image.mode == "L":
            image = image.convert("RGBA")

        image2 = image.convert("RGBA")
        data = image2.tobytes("raw", "RGBA")
        qim = QImage(data, image.size[0], image.size[1], QImage.Format_ARGB32)
        pixmap = QPixmap.fromImage(qim)

        self.setPixmap(QPixmap(pixmap))
        self.mainWindow.ui.label_image_output.setPixmap(QPixmap(pixmap))
        self.switch = 1

    def mousePressEvent(self, event):
        if self.switch:
            self.mainWindow.get(event.pos())
