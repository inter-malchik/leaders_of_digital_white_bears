import os
import sys

from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QLabel, QGraphicsDropShadowEffect, QGridLayout, \
    QSpacerItem, QSizePolicy, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtCore

from gui import Ui_MainWindow
from slider import Ui_MainWindow as SliderWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # self.setStyleSheet(Stylesheet)
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(2, 2)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)

        # self.widget = QWidget(self)
        # self.widget.setObjectName('Custom_Widget')
        # layout = QVBoxLayout(self)
        # layout.addWidget(self.widget)
        #
        # layout = QGridLayout(self)
        # close_button = QPushButton()
        # close_button.clicked.connect(self.exit)
        # # close_button.setObjectName('closeButton')
        # layout.addItem(QSpacerItem(
        #     40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, 0)
        # layout.addWidget(close_button, 0, 1)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.setFixedSize(QSize(492, 308))
        self.setWindowTitle('Медведи')


    def connectSignalsSlots(self):
        self.directoryButton.clicked.connect(self.create_choosing_dir)
        self.handlerButton.clicked.connect(self.handler)
        self.directoryButton_2.clicked.connect(self.create_choosing_dir_2)
        self.closeButton.clicked.connect(self.close)

    def create_choosing_file(self):
        file_window = QFileDialog()
        filepath = file_window.getOpenFileUrl()
        self.lineEdit.setText(filepath[0].toString()[8:])

    def create_choosing_dir(self):
        dir_window = QFileDialog()
        dirpath = dir_window.getExistingDirectoryUrl()
        self.lineEdit.setText(dirpath.toString()[8:])

    def create_choosing_file_2(self):
        file_window = QFileDialog()
        filepath = file_window.getOpenFileUrl()
        self.saveToLineEdit.setText(filepath[0].toString()[8:])

    def create_choosing_dir_2(self):
        dir_window = QFileDialog()
        dirpath = dir_window.getExistingDirectoryUrl()
        self.saveToLineEdit.setText(dirpath.toString()[8:])

    def handler(self):
        self.close()
        self.slider_wind = Slider(self.lineEdit.text())
        self.slider_wind.show()

    def exit(self):
        self.close()


class Slider(QMainWindow, SliderWindow):
    def __init__(self, path, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.set_path(path)
        self.setFixedSize(QSize(986, 563))
        self.set_first_photo()
        self.setWindowTitle('Найденные медведи')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # self.setStyleSheet(Stylesheet)
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(2, 2)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)


    @classmethod
    def set_path(cls, path):
        cls.files = os.listdir(path)
        cls.files.sort()
        cls.pointer = 0
        cls.path = path

    def next(self):
        if self.pointer!=len(self.files)-1:
            path = self.path + '/' + self.files[self.pointer+1]
            pixmap = QPixmap(path)
            self.lbl.setPixmap(pixmap)
            self.pointer += 1
            self.prevButton.setEnabled(True)
        if self.pointer==len(self.files)-1:
            self.nextButton.setEnabled(False)

    def prev(self):
        if self.pointer!=0:
            path = self.path + '/' + self.files[self.pointer-1]
            pixmap = QPixmap(path)
            self.lbl.setPixmap(pixmap)
            self.nextButton.setEnabled(True)
            self.pointer -= 1
        if self.pointer==0:
            self.prevButton.setEnabled(False)

    def connectSignalsSlots(self):
        self.nextButton.clicked.connect(self.next)
        self.prevButton.clicked.connect(self.prev)
        self.backButton.clicked.connect(self.back)
        self.closeButton.clicked.connect(self.close)

    def set_first_photo(self):
        self.lbl = QLabel(self)
        path = self.path + '/' + self.files[self.pointer]
        pixmap = QPixmap(path)
        self.lbl.setPixmap(pixmap)
        self.photoLayot.addWidget(self.lbl)
        self.pointer += 1
        self.prevButton.setEnabled(False)

    def back(self):
        self.close()
        self.main = Window()
        self.main.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    file = QtCore.QFile("styles.qss")  # !!! dark.qss
    file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    stream = QtCore.QTextStream(file)
    app.setStyleSheet(stream.readAll())
    win = Window()
    win.show()
    sys.exit(app.exec())