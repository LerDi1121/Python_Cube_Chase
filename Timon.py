"""vujadin"""
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import *

class Timon(QFrame):
        PumbaWidth = 40
        PumbaHeight = 40
        pX = 10
        pY = 20

        LabelTimon = 0
        Picture = ""

        def __init__(self, parent, x, y, picture):
            super(parent,self).__init__()

            self.initTimon(parent, x, y, picture)

        def initTimon(self, parent, x, y, picture):
            self.resize(800, 600)
            self.pX = x
            self.pY = y
            self.Picture = picture

            self.LabelTimon = QLabel(parent)

            PixmapTimon = QPixmap(picture)
            PixmapResizedTimon = PixmapTimon.scaled(self.TimonWidth,self.TimonHeight)

            self.LabelTimon.setPixmap(PixmapResizedPumba)
            self.LabelTimon.move(x, y)

        def updatePosition(self, x, y):
            self.pX = x
            self.pY = y

            self.LabelTimon.move(x, y)






