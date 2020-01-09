"""vujadin"""
from random import randint

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
        Speed = 0.3
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

            PixmapEnemy = QPixmap(picture)
            PixmapResizedEnemy = PixmapEnemy.scaled(self.EnemyWidth, self.EnemyHeight)

            self.LabelEnemy.setPixmap(PixmapResizedEnemy)
            self.LabelEnemy.move(x, y)

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
                value2 = randint(1, 15)
                if value == 0:
                    for x in range(value2):
                        if Enemy.pX > 10:
                            newX = self.pX - 40
                            if (newX, newY) not in Map.Walls:
                                self.updatePosition(newX, newY)
                                #time.sleep(Enemy.Speed)
                if value == 1:
                    for x in range(value2):
                        if Enemy.pX < 770:
                            newX = self.pX + 40
                            if (newX, newY) not in Map.Walls:
                                Enemy.updatePosition(newX, newY)
                             # time.sleep(Enemy.Speed)
                if value == 2:
                    for x in range(value2):
                        if Enemy.pY > 10:
                            newY = Enemy.pY - 40
                            if (newX, newY) not in Map.Walls:
                                Enemy.updatePosition(newX, newY)
                                #time.sleep(Enemy.Speed)
                if value == 3:
                    for x in range(value2):
                        if Enemy.pY < 570:
                            newY = Enemy.pY + 40
                            if (newX, newY) not in Map.Walls:
                                Enemy.updatePosition(newX, newY)
                                #time.sleep(Enemy.Speed)

        def timerEvent(self, a0: 'QTimerEvent'):
            self.move.emit()




