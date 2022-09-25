import sys
from PyQt5.QtCore import pyqtSignal, Qt, QThread
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QSplashScreen, QMainWindow

class Worker(QThread):
    progressChanged = pyqtSignal(int)

    def run(self):
        for count in range(6):
            self.progressChanged.emit(count)
            self.sleep(1)
        self.progressChanged.emit(-1)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

class SplashScreen(QSplashScreen):
    def __init__(self, filepath, flags=0):
        super().__init__(flags=Qt.WindowFlags(flags))
        self.movie = QMovie(filepath, parent=self)
        self.movie.frameChanged.connect(self.handleFrameChange)
        self.movie.start()

    def updateProgress(self, count=0):
        if count == 0:
            message = 'Starting...'
        elif count > 0:
            message = f'Processing... {count}'
        else:
            message = 'Finished!'
        self.showMessage(
            message, Qt.AlignHCenter | Qt.AlignBottom, Qt.white)

    def handleFrameChange(self):
        pixmap = self.movie.currentPixmap()
        self.setPixmap(pixmap)
        self.setMask(pixmap.mask())

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    splash = SplashScreen('anim.gif', Qt.WindowStaysOnTopHint)
    worker = Worker()
    worker.progressChanged.connect(splash.updateProgress)
    worker.finished.connect(
        lambda: (splash.finish(window), window.show()))
    splash.show()
    worker.start()
    app.exec_()