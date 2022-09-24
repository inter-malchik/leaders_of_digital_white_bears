import sys

from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

from gui import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.fileButton.clicked.connect(self.create_choosing_file)
        self.directoryButton.clicked.connect(self.create_choosing_dir)
        self.handlerButton.clicked.connect(self.handler)

    def create_choosing_file(self):
        file_window = QFileDialog()
        filepath = file_window.getOpenFileUrl()
        self.lineEdit.setText(filepath[0].toString()[8:])

    def create_choosing_dir(self):
        dir_window = QFileDialog()
        dirpath = dir_window.getExistingDirectoryUrl()
        self.lineEdit.setText(dirpath.toString()[8:])

    def handler(self):
        print(self.lineEdit.text())










if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())