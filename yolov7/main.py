import os
import sys
from time import sleep

from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QLabel, QGraphicsDropShadowEffect, QGridLayout, \
    QSpacerItem, QSizePolicy, QPushButton, QWidget, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QMovie
from PyQt5.QtCore import QSize, Qt, QThread, pyqtSignal, QObject
from PyQt5 import QtCore

from GUI import Ui_MainWindow
from slider import Ui_MainWindow as SliderWindow
from loading import Ui_MainWindow as LoadingWindow

from model import ModelWork as model_class


class Loading(QMainWindow, LoadingWindow):
    def __init__(self, path=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(2, 2)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)
        # self.setFixedSize(QSize(492, 308))
        self.setWindowTitle('Загрузка')
        self.hui = r""



class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(2, 2)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)
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
        self.loadWind = Loading(self.lineEdit.text())
        self.loadWind.show()
        model = model_class(self.lineEdit.text(), self.saveToLineEdit.text())
        model.puck_data_processing(model.data_folder_path)
        self.slider_wind = Slider(self.saveToLineEdit.text())
        self.loadWind.close()
        self.slider_wind.show()

    def exit(self):
        self.close()


class Slider(QMainWindow, SliderWindow):
    def __init__(self, path, pointer=0, parent=None):
        super().__init__(parent)
        self.files = []
        self.pointer = pointer
        self.setupUi(self)
        self.connectSignalsSlots()
        self.set_path(path)
        self.setFixedSize(QSize(986, 563))
        self.set_first_photo()
        self.setWindowTitle('Найденные медведи')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(2, 2)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)
        self.backButton.setIcon(QIcon('icon_back.png'))

    def set_path(self, path):
        self.files = os.listdir(path)
        self.files.sort()
        self.path = path

    def next(self):
        if self.pointer!=len(self.files)-1:
            self.pointer += 1
            path = self.path + '/' + self.files[self.pointer]
            pixmap = QPixmap(path)
            self.lbl.setPixmap(pixmap)
            self.prevButton.setEnabled(True)
        if self.pointer==len(self.files)-1:
            self.nextButton.setEnabled(False)

    def prev(self):
        if self.pointer!=0:
            self.pointer -= 1
            path = self.path + '/' + self.files[self.pointer]
            pixmap = QPixmap(path)
            self.lbl.setPixmap(pixmap)
            self.nextButton.setEnabled(True)
        if self.pointer==0:
            self.prevButton.setEnabled(False)

    def connectSignalsSlots(self):
        self.nextButton.clicked.connect(self.next)
        self.prevButton.clicked.connect(self.prev)
        self.backButton.clicked.connect(self.back)
        self.closeButton.clicked.connect(self.close)
        self.removeButton.clicked.connect(self.remove)

    def set_first_photo(self):
        if len(self.files)!=0:
            path = self.path + '/' + self.files[self.pointer]
        else:
            path = 'not_photos.jpg'
            self.prevButton.setEnabled(False)
            self.nextButton.setEnabled(False)
            self.removeButton.setEnabled(False)
        self.lbl = QLabel(self)
        pixmap = QPixmap(path)
        self.lbl.setPixmap(pixmap)
        self.photoLayot.addWidget(self.lbl)
        self.prevButton.setEnabled(False)

    def back(self):
        self.close()
        self.main = Window()
        self.main.show()

    def remove(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("Ты действительно хочешь удалить эту фотографию?")
        msgBox.setWindowTitle("Подтвердите удаление")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if msgBox.exec() == QMessageBox.Ok:
            os.remove(self.path+'/'+self.files[self.pointer])
            if self.pointer==len(self.files)-1:
                path = self.path + '/' + self.files[self.pointer-1]
                self.files.pop(self.pointer)
                self.close()
                self.new = Slider(self.path)
                self.new.show()
            else:
                path = self.path + '/' + self.files[self.pointer + 1]
                self.files.pop(self.pointer)
                self.close()
                self.new = Slider(self.path)
                self.new.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    file = QtCore.QFile("styles.qss")
    file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    stream = QtCore.QTextStream(file)
    app.setStyleSheet(stream.readAll())
    win = Window()
    win.show()
    sys.exit(app.exec_())