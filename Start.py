from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import *
from Player  import *
from Timon import *
from Pumba import *

import sys

from PyQt5.uic.properties import QtGui


class LavirintP(QMainWindow):
    def __init__(self):

        super(LavirintP, self).__init__()
        self.InitStart()
        self.PlayerDist = {}
        self.EnemyPumba = None
        self.EnemyTimon = None
        self.createPlayerAndEnemy()
        self.show()

    def InitStart(self):
        self.resize(800, 600)
        self.center()
        self.setWindowTitle("Cub Chase")
        self.center()
        hbox = QHBoxLayout(self)
        pixmap = QPixmap('images\pozadinaProba.png')
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        QLabel.setGeometry(lbl, 0, -6, 800, 600)
        hbox.addWidget(lbl)
        self.resize(pixmap.width(), pixmap.height())
        self.setLayout(hbox)

    def createPlayerAndEnemy(self):
        self.PlayerDist[0] = Player(self, 100, 100, 'images\Simba.png')
        self.PlayerDist[1] = Player(self, 100, 200, 'images\imgNela.png')
        self.EnemyTimon = Timon(self, 200, 100, 'images\imgTimon.png')
        self.EnemyPumba = Pumba(self, 200, 200, 'images\pumba.png')
    def center(self):

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = LavirintP()
    sys.exit(app.exec_())