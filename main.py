# -*- coding: utf-8 -*-
import sys
import base64
from io import BytesIO
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from UI import Ui_MainWindow
from dropLabel import dLabel
from pic2str import arrow
from PIL import Image, ImageQt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initialArrowIcon()
        self.setFixedSize(self.size())

        # Add pLabel & delete old QLabel
        self.label_image_original = dLabel(self.ui.centralwidget, self)
        self.label_image_original.setGeometry(QRect(
            self.ui.label_image_original.pos(),
            self.ui.label_image_original.size()))

        del self.ui.label_image_original

        # Button
        self.ui.pushButton_upload.clicked.connect(self.openFileEvent)
        self.ui.pushButton_exit.clicked.connect(self.exitEvent)
        self.ui.pushButton_save.clicked.connect(self.saveEvent)

        # Slider
        self.ui.horizontalSlider_R.setDisabled(True)
        self.ui.horizontalSlider_G.setDisabled(True)
        self.ui.horizontalSlider_B.setDisabled(True)

        self.ui.horizontalSlider_R.setMaximum(255)
        self.ui.horizontalSlider_G.setMaximum(255)
        self.ui.horizontalSlider_B.setMaximum(255)
        self.ui.horizontalSlider_R.valueChanged.connect(lambda: self.color_value('R'))
        self.ui.horizontalSlider_G.valueChanged.connect(lambda: self.color_value('G'))
        self.ui.horizontalSlider_B.valueChanged.connect(lambda: self.color_value('B'))

        # LineEdit
        self.ui.lineEdit_R.textChanged.connect(self.color_change)
        self.ui.lineEdit_G.textChanged.connect(self.color_change)
        self.ui.lineEdit_B.textChanged.connect(self.color_change)

    def changeOutputColor(self):
        image = ImageQt.fromqpixmap(self.ui.label_image_output.pixmap())
        image = image.resize((self.ui.label_image_output.size().width(), self.ui.label_image_output.size().height()))
        image_data = list(image.getdata())

        newRGBA = (self.newR, self.newG, self.newB, self.rgba[3])
        for index in self.changePos:
            image_data[index] = newRGBA

        image.putdata(image_data)

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

        self.ui.label_image_output.setPixmap(QPixmap(pixmap))

    def get(self, pos):
        index = pos.y() * self.label_image_original.size().width() + pos.x()
        image = ImageQt.fromqpixmap(self.label_image_original.pixmap())
        image = image.resize((self.label_image_original.size().width(), self.label_image_original.size().height()))
        image_data = image.getdata()

        self.rgba = image_data[index]
        if len(self.rgba) == 3:
            r, g, b = self.rgba
        elif len(image_data[index]) == 4:
            r, g, b, a = self.rgba

        self.changePos = []

        index = 0
        for item in image_data:
            if item == self.rgba:
                self.changePos.append(index)

            index += 1

        print(len(self.changePos))
        print(self.changePos)
        self.ui.label_color_original.setStyleSheet('background-color: rgb({},{},{});'.format(r, g, b))
        self.ui.horizontalSlider_R.setDisabled(False)
        self.ui.horizontalSlider_G.setDisabled(False)
        self.ui.horizontalSlider_B.setDisabled(False)

    def color_change(self):
        self.newR = int(self.ui.lineEdit_R.text())
        self.newG = int(self.ui.lineEdit_G.text())
        self.newB = int(self.ui.lineEdit_B.text())
        self.ui.label_color_output.setStyleSheet('background-color: rgb({}, {}, {});'.format(
            self.newR,
            self.newG,
            self.newB
        ))
        self.changeOutputColor()

    def color_value(self, color):
        if color == 'R':
            self.ui.lineEdit_R.setText(str(self.ui.horizontalSlider_R.value()))
        elif color == 'G':
            self.ui.lineEdit_G.setText(str(self.ui.horizontalSlider_G.value()))
        elif color == 'B':
            self.ui.lineEdit_B.setText(str(self.ui.horizontalSlider_B.value()))

    def openFileEvent(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", QDir.homePath())

        if file_name.split('.')[-1] in ['png', 'jpg', 'jpeg']:
            image = Image.open(file_name)
            image = image.resize((self.ui.label_image_output.size().width(), self.ui.label_image_output.size().height()))

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

            self.label_image_original.setPixmap(QPixmap(pixmap))
            self.ui.label_image_output.setPixmap(QPixmap(pixmap))
            self.label_image_original.switch = 1


    def initialArrowIcon(self):
        # Load byte data
        byte_data = base64.b64decode(arrow)
        image_data = BytesIO(byte_data)
        image = Image.open(image_data)
        image = image.convert('RGBA')

        # PIL to QPixmap
        qImage = ImageQt.ImageQt(image)
        image = QPixmap.fromImage(qImage)

        self.ui.label_arrow.setPixmap(QPixmap(image))
        self.ui.label_arrow.setScaledContents(True)

    def saveEvent(self):
        image = ImageQt.fromqpixmap(self.ui.label_image_output.pixmap())
        image.save('test.png')

    def exitEvent(self):
        exit()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())