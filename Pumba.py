
from random import randint
import time
from threading import Thread

from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, QTimer, QEventLoop
from PyQt5.QtGui import *

import Map

class Enemy(QFrame):
        EnemyWidth = 40
        EnemyHeight = 40
        pX = 0
        pY = 0
        LabelEnemy = 0
        Picture = ""
        Speed = 0.3
        ID = 0
        CanMove = True
        Move = pyqtSignal()
        inTrap = pyqtSignal()

        def __init__(self, parent, x, y, picture, id):
            super().__init__(parent)

            self.initEnemy(parent, x, y, picture, id)

        def initEnemy(self, parent, x, y, picture, id):
            self.resize(40, 40)
            self.pX = x
            self.pY = y
            self.Picture = picture
            self.ID = id
            self.LabelEnemy = QLabel(parent)
            self.Move.connect(self.moveEnemy)
            self.inTrap.connect(self.inTrap2)
            PixmapEnemy = QPixmap(picture)
            PixmapResizedEnemy = PixmapEnemy.scaled(self.EnemyWidth, self.EnemyHeight)

            self.LabelEnemy.setPixmap(PixmapResizedEnemy)
            self.timer = QBasicTimer()
            self.timer.start(10, self) #na svakid 10 milisek on mu apdejtuje poziciju bez obzira da li su se promenile koord.
            self.LabelEnemy.move(x, y)


        def inTrap2(self):
            self.CanMove= False
            thread1 = Thread(target=self.inTrapforThread)
            thread1.start()

        def inTrapforThread(self):
            time.sleep(10)
            self.CanMove = True

        def changeCoord(self):
           while True:
                val1 = randint(1, 4)
                val2 = randint(1, 15)
                if self.CanMove == True:
                    if val1 % 4 == 0:
                        for x in range(val2):
                            if self.pX > 10:
                                if (self.pX-40, self.pY) not in Map.Map.Walls:
                                    if self.CanMove == True:
                                        self.pX= self.pX-40
                                        time.sleep(self.Speed)
                    if val1 % 4 == 1:
                        for x in range(val2):
                            if self.pX < 770:
                                if (self.pX + 40, self.pY) not in Map.Map.Walls:
                                    if self.CanMove == True:
                                        self.pX = self.pX +40
                                        time.sleep(self.Speed)

                    if val1 % 4 == 2:
                        for x in range(val2):
                            if self.pY > 10:
                                if (self.pX, self.pY - 40) not in Map.Map.Walls:
                                    if self.CanMove == True:
                                        self.pY = self.pY - 40
                                        time.sleep(self.Speed)

                    if val1 % 4 == 3:
                        for x in range(val2):
                            if self.pY < 570:
                                if (self.pX, self.pY + 40) not in Map.Map.Walls:
                                    if self.CanMove == True:
                                        self.pY = self.pY + 40
                                        time.sleep(self.Speed)


        def moveEnemy(self):
            self.LabelEnemy.move(self.pX, self.pY)

        def timerEvent(self, event):
            self.Move.emit()
