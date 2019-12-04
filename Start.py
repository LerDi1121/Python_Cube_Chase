from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QWidget
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor
import sys

from PyQt5.uic.properties import QtGui


class LavirintP(QMainWindow):
    def __init__(self):

        super(LavirintP, self).__init__()
        self.resize(700, 650)
        self.center()
        self.setWindowTitle("Cub Chase")
        self.center()
        self.show()

    def center(self):

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,(screen.height() - size.height()) / 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = LavirintP()
    sys.exit(app.exec_())