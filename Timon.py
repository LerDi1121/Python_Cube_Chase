"""vujadin"""
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import *

class Timon(QFrame):
        TimonWidth = 40
        TimonHeight = 40
        pX = 10
        pY = 20
        CanMove = True;
        LabelTimon = 0
        Picture = ""

        def __init__(self, parent, x, y, picture):
            super().__init__(parent)

            self.initTimon(parent, x, y, picture)

        def initTimon(self, parent, x, y, picture):
            self.resize(800, 600)
            self.pX = x
            self.pY = y
            self.Picture = picture

            self.LabelTimon = QLabel(parent)

            PixmapTimon = QPixmap(picture)
            PixmapResizedTimon = PixmapTimon.scaled(self.TimonWidth, self.TimonHeight)

            self.LabelTimon.setPixmap(PixmapResizedTimon)
            self.LabelTimon.move(x, y)

        def updatePosition(self, x, y):
            self.pX = x
            self.pY = y
            PixmapTimon = QPixmap(self.Picture)
            PixmapResizedTimon = PixmapTimon.scaled(self.TimonWidth, self.TimonHeight)

            self.LabelTimon.setPixmap(PixmapResizedTimon)
            self.LabelTimon.move(x, y)






