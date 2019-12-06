"""vujadin"""
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import *

class Pumba(QFrame):
        PumbaWidth = 40
        PumbaHeight = 40
        pX = 0
        pY = 0

        LabelPumba = 0
        Picture = ""

        def __init__(self, parent, x, y, picture):
            super(parent,self).__init__()

            self.initPumba(parent, x, y, picture)

        def initPumba(self, parent, x, y, picture):
            self.resize(800, 600)
            self.pX = x
            self.pY = y
            self.Picture = picture

            self.LabelPumba = QLabel(parent)

            PixmapPumba = QPixmap(picture)
            PixmapResizedPumba = PixmapPumba.scaled(self.PumbaWidth,self.PumbaHeight)

            self.LabelPumba.setPixmap(PixmapResizedPumba)
            self.LabelPumba.move(x, y)

        def updatePosition(self, x, y):
            self.pX = x
            self.pY = y

            self.LabelPumba.move(x, y)






