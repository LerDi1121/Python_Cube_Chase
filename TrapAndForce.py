import time

from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, QEventLoop, QTimer
from PyQt5.QtGui import *
from Map import *





class TrapAndForce(QFrame):
    pX=0
    pY=0
    picture= ""
    TrapOrForce= 1

    isActive= False
    deactiveTrap= pyqtSignal()
    activeTrap= pyqtSignal()

    def __init__(self, parent, x, y,  id, tf):
        super().__init__(parent)

        self.initTrapAndForce(parent, x, y,  id, tf)
    def initTrapAndForce(self, parent,x,y, id, tf):
        self.pX=x
        self.pY=y
        self.ID= id
        self.activeTrap.connect(self.active)
        self.deactiveTrap.connect(self.deactive)
        self.TrapOrForce= tf
        self.Label = QLabel(parent)
        Pixmap = QPixmap("images\zamkaNeaktivna.png")
        PixmapResized = Pixmap.scaled(40,40)
        self.Label.setPixmap(PixmapResized)
        self.Label.move(x, y)


    def trap(self, enemy):
        print("")
    def deactive(self):
        Pixmap = QPixmap("images\zamkaNeaktivna.png")
        PixmapResized = Pixmap.scaled(40, 40)
        self.Label.setPixmap(PixmapResized)
        self.isActive = False
    def active(self):
        self.isActive= True
        Pixmap = QPixmap("images\zamkaAktivna.png")
        PixmapResized = Pixmap.scaled(40, 40)
        self.Label.setPixmap(PixmapResized)
        loop = QEventLoop()
        QTimer.singleShot(10000, loop.quit)
        loop.exec_()
        Pixmap = QPixmap("images\zamkaNeaktivna.png")
        PixmapResized = Pixmap.scaled(40, 40)
        self.Label.setPixmap(PixmapResized)
        self.isActive = False

    def force(self, player):
        print("")
