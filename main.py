import sys

from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5 import QtGui

from gui import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.create_choosing_file)

    def create_choosing_file(self):
        file_window = QFileDialog()
        filepath = file_window.getOpenFileUrl()
        print(filepath)
        self.lineEdit.setText(filepath[0].toString())






if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())