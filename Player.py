"""vujadin"""
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import *

class Player(QFrame):
        PlayerWidth = 40
        PlayerHeight = 40
        pX = 0
        pY = 0

        LabelPlayer = 0
        Picture = ""
        ID = 0
        CanMove = True
        IsAlive = True

        def __init__(self, parent, x, y, picture, id):
            super().__init__(parent)

            self.initPlayer(parent, x, y, picture, id)

        def initPlayer(self, parent, x, y, picture, id):
            self.resize(800, 600)
            self.pX = x
            self.pY = y
            self.Picture = picture

            self.LabelPlayer = QLabel(parent)

            PixmapPlayer = QPixmap(picture)
            PixmapResizedPlayer = PixmapPlayer.scaled(self.PlayerWidth,self.PlayerHeight)

            self.LabelPlayer.setPixmap(PixmapResizedPlayer)
            self.LabelPlayer.move(x, y)

        def updatePosition(self, x, y):
            self.pX = x
            self.pY = y

            PixmapPlayer = QPixmap(self.Picture)
            PixmapResizedPlayer = PixmapPlayer.scaled(self.PlayerWidth, self.PlayerHeight)

            self.LabelPlayer.setPixmap(PixmapResizedPlayer)

            self.LabelPlayer.move(x, y)






