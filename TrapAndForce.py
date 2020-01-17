import time
from random import randint
from threading import Thread

from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, QEventLoop, QTimer
from PyQt5.QtGui import *
from Map import *

class TrapAndForce(QFrame):
    pX = 0
    pY = 0
    picture = ""
    TrapOrForce = 1
    space = []
    isActive = False
    deactiveTrap = pyqtSignal()
    activeTrap = pyqtSignal()

    def __init__(self, parent,  id, tf):  #poslednji param. je da li je sila ili zamka
        super().__init__(parent)

        self.initTrapAndForce(parent,  id, tf)

    def initTrapAndForce(self, parent, id, tf):
        for x in range(len(Map.Level)):
            for y in range(len(Map.Level[x])):
                character = Map.Level[x][y]
                if character != "X":
                    coordX = x * 40 + 10
                    coordY = y * 40 + 10
                    self.space.append((coordY, coordX))
        val = randint(0,len(self.space))
        (self.pX,self.pY)= self.space[val]
        self.ID = id
        self.activeTrap.connect(self.active)
        self.deactiveTrap.connect(self.deactive)
        self.TrapOrForce = tf
        self.Label = QLabel(parent)
        if self.TrapOrForce==2:
            Pixmap = QPixmap("images\ihvhhjb.png")
        else:
            Pixmap = QPixmap("images\zamkaNeaktivna.png")
        PixmapResized = Pixmap.scaled(40,40)
        self.Label.setPixmap(PixmapResized)
        self.Label.move(self.pX, self.pY)

    def deactive(self): # zamka
        Pixmap = QPixmap("images\zamkaNeaktivna.png")
        PixmapResized = Pixmap.scaled(40, 40)
        self.Label.setPixmap(PixmapResized)
        self.isActive = False

    def active(self): #zamka
        if self.isActive==False:
            self.isActive= True
            Pixmap = QPixmap("images\zamkaAktivna.png")
            PixmapResized = Pixmap.scaled(40, 40)
            self.Label.setPixmap(PixmapResized)
            thread1 = Thread(target=self.activeForThread)
            thread1.start()

    def activeForThread(self): #zamka
        time.sleep(10)
        Pixmap = QPixmap("images\zamkaNeaktivna.png")
        PixmapResized = Pixmap.scaled(40, 40)
        self.Label.setPixmap(PixmapResized)
        self.isActive = False

    def activeForce(self):
        val = randint(0,len(self.space))
        (self.pX,self.pY)= self.space[val]

        Pixmap = QPixmap("images\imgUpitnik.png")
        PixmapResized = Pixmap.scaled(40, 40)
        self.Label.setPixmap(PixmapResized)
        self.Label.move(self.pX, self.pY)

    def deactiveForce(self):
        Pixmap = QPixmap("images\zimggdfgdUpik.png")
        PixmapResized = Pixmap.scaled(40, 40)
        self.Label.setPixmap(PixmapResized)

