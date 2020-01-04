"""vujadin"""
from random import randint
import time
from threading import Thread

from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import *

import Map


class Enemy(QFrame):
        EnemyWidth = 40
        EnemyHeight = 40
        pX = 0
        pY = 0
        CanMove= True
        LabelEnemy = 0
        Picture = ""
        Speed = 300
        ID =0
        Move = pyqtSignal()

        def __init__(self, parent, x, y, picture, id):
            super().__init__(parent)

            self.initEnemy(parent, x, y, picture,id)

        def initEnemy(self, parent, x, y, picture, id):
            self.resize(800, 600)
            self.pX = x
            self.pY = y
            self.Picture = picture
            self.ID=id
            self.LabelEnemy = QLabel(parent)
            self.Move.connect(self.moveEnemy)
            PixmapEnemy = QPixmap(picture)
            PixmapResizedEnemy = PixmapEnemy.scaled(self.EnemyWidth, self.EnemyHeight)

            self.LabelEnemy.setPixmap(PixmapResizedEnemy)
            self.timer = QBasicTimer()
            self.timer.start(self.Speed, self)
            self.LabelEnemy.move(x, y)
            #self.t = Thread(target=self.moveEnemy)
            #self.t.daemon = True
            #self.t.start()

        # T4.start()

        def updatePosition(self, x, y):
            self.pX = x
            self.pY = y
            PixmapEnemy = QPixmap(self.Picture)
            PixmapResizedEnemy = PixmapEnemy.scaled(self.EnemyWidth, self.EnemyHeight)
            self.LabelEnemy.setPixmap(PixmapResizedEnemy)
            self.LabelEnemy.move(x, y)




        def moveEnemy(self):
            if self.CanMove:
                newX = self.pX
                newY = self.pY
                value = randint(0, 3)

                if value == 0:
                    if newY > 10:
                        newY = newY - 40
                        if (newX, newY) not in Map.Map.Walls:
                            self.LabelEnemy.move(newX, newY)
                            self.pX = newX
                            self.pY = newY
                if value == 1:
                    if newY < 570:
                        newY = newY + 40
                        if (newX, newY) not in Map.Map.Walls:
                            self.LabelEnemy.move(newX, newY)
                            self.pX = newX
                            self.pY = newY

                if value == 2:
                    if newX > 10:
                        newX = newX - 40
                        if (newX, newY) not in Map.Map.Walls:
                            self.LabelEnemy.move(newX, newY)
                            self.pX = newX
                            self.pY = newY

                if value == 3:
                    if newX < 770:
                        newX = newX + 40
                        if (newX, newY) not in Map.Map.Walls:
                            self.LabelEnemy.move(newX, newY)
                            self.pX = newX
                            self.pY = newY





        def timerEvent(self, event):
            self.Move.emit()




