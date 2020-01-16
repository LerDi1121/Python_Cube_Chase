import time
from threading import Thread

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

    def __init__(self, parent, x, y,  id, tf):  #poslednji param. je da li je sila ili zamka
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

    def deactive(self):
        Pixmap = QPixmap("images\zamkaNeaktivna.png")
        PixmapResized = Pixmap.scaled(40, 40)
        self.Label.setPixmap(PixmapResized)
        self.isActive = False

    def active(self):
        if self.isActive==False:
            self.isActive= True
            Pixmap = QPixmap("images\zamkaAktivna.png")
            PixmapResized = Pixmap.scaled(40, 40)
            self.Label.setPixmap(PixmapResized)
            thread1 = Thread(target=self.activeForThread)
            thread1.start()

    def activeForThread(self):
        time.sleep(10)
        Pixmap = QPixmap("images\zamkaNeaktivna.png")
        PixmapResized = Pixmap.scaled(40, 40)
        self.Label.setPixmap(PixmapResized)
        self.isActive = False


    def force(self, player):
        print("")
