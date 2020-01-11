from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import *
from Map import *

class footPrint(QFrame):

    pX=0
    pY=0

    def __init__(self, parent, x, y):
        super().__init__(parent)



        self.pX = x
        self.pY = y
        self.picture = QLabel(self)
        print("sdasdasd")
        Slika = QPixmap('images\imgfoot1_small.png')
        PixmapResizedEnemy = Slika.scaled(40, 40)
        self.picture.setPixmap(PixmapResizedEnemy)
        self.picture.move(self.pX, self.pY)








