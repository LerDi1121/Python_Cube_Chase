from random import randint

from PyQt5.QtWidgets import QMainWindow, QGridLayout, QFrame, QDesktopWidget, QApplication, QWidget, QHBoxLayout, QLabel, QFileDialog
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import *
from Player  import *
from Timon import *
from Pumba import *
from threading import Thread, Timer
from Command import *
import time
import sys
import keyboard
from Map import *
import uuid

import multiprocessing as mp

from PyQt5.uic.properties import QtGui


class LavirintP(QMainWindow):
    def __init__(self):

        self.Walls=[]
        self.Grass=[]
        self.Space=[]
        self.UseSpace=[]
        super(LavirintP, self).__init__()
        self.InitStart()
        self.PlayerDict = {}
        self.EnemyPumba = None
        self.EnemyTimon = None
        self.createPlayerAndEnemy()
        self.createLabels()

        T1 =Thread(target=self.keyEvent)
        T1.daemon = True
        T1.start()

        T2=Thread(target=self.keyEvent2)
        T2.daemon = True
        T2.start()

        T3=Thread(target=self.enemyMove)
        T3.daemon = True
        T3.start()

        T4=Thread(target=self.enemyMove2)
        T4.daemon = True
        T4.start()

        T5 = Thread(target=self.playerDead)
        T5.daemon = True
        T5.start()

        self.show()

    def InitStart(self):
        self.resize(820, 620)
        self.center()
        self.setWindowTitle("Cub Chase")
        self.center()
        hbox = QHBoxLayout(self)

        pixmap = QPixmap('images\imgBackground2.png')
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        QLabel.setGeometry(lbl, 0, 0, 820, 620)
        hbox.addWidget(lbl)
        self.resize(pixmap.width(), pixmap.height())
        self.setLayout(hbox)
        self.wall()


    def createPlayerAndEnemy(self):

        self.PlayerDict[0] = Player(self, 770, 570, 'images\Simba.png', 'images\imgfoot1_small.png', 0)
        self.PlayerDict[1] = Player(self, 10, 570, 'images\imgNala.png', 'images\imgfoot2_small.png',  1)
        self.EnemyTimon = Timon(self, 10, 10, 'images\imgTimon.png')
        self.EnemyPumba = Pumba(self, 770, 10, 'images\pumba.png')

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def wall(self):
        for x in range (len( Map.Level)):
            for y in range(len(Map.Level[x])):
                character = Map.Level[x][y]
                if character == "X":
                    coordX = x * 40 + 10
                    coordY = y * 40 + 10
                    self.Walls.append((coordY, coordX))
                if character == "G":
                    coordX = x * 40 + 10
                    coordY = y * 40 + 10
                    self.Grass.append((coordY, coordX))
                if character == " ":
                    coordX = x * 40 + 10
                    coordY = y * 40 + 10

                    self.Space.append((coordY, coordX))


    def tryMoveTimon(self, Timon, KeyStroke):
        newX = Timon.pX
        newY = Timon.pY

        if Timon.CanMove == True:
            if KeyStroke == myCommand.Left:
                if Timon.pX> 10:
                     newX = Timon.pX - 40
                     if(newX,newY) not in self.Walls:
                         Timon.updatePosition(newX, newY)
                         return True
                     else:
                         return False
                else:
                    return False
            elif KeyStroke == myCommand.Right:
                if Timon.pX <770:
                     newX = Timon.pX + 40
                     if (newX, newY) not in self.Walls:
                        Timon.updatePosition(newX, newY)
                        return True
                     else:
                        return False
                else:
                    return False
            elif KeyStroke == myCommand.Up:
                if Timon.pY >10:
                     newY = Timon.pY - 40
                     if (newX, newY) not in self.Walls:
                         Timon.updatePosition(newX, newY)
                         return True
                     else:
                         return False
                else:
                    return False
            elif KeyStroke == myCommand.Down:
                if Timon.pY < 570:
                     newY = Timon.pY + 40
                     if (newX, newY) not in self.Walls:
                         Timon.updatePosition(newX, newY)
                         return True
                     else:
                         return False
                else:
                    return False
        else:
            return False

    def tryMovePumba(self, Pumba, KeyStroke):
        newX = Pumba.pX
        newY = Pumba.pY

        if Pumba.CanMove == True:
            if KeyStroke == myCommand.Left:
                if Pumba.pX > 10:
                    newX = Pumba.pX - 40
                    if (newX, newY) not in self.Walls:
                        Pumba.updatePosition(newX, newY)
                        return True
                    else:
                        return False
                else:
                    return False
            elif KeyStroke == myCommand.Right:
                if Pumba.pX < 770:
                    newX = Pumba.pX + 40
                    if (newX, newY) not in self.Walls:
                        Pumba.updatePosition(newX, newY)
                        return True
                    else:
                        return False
                else:
                    return False
            elif KeyStroke == myCommand.Up:
                if Pumba.pY > 10:
                    newY = Pumba.pY - 40
                    if (newX, newY) not in self.Walls:
                        Pumba.updatePosition(newX, newY)
                        return True
                    else:
                        return False
                else:
                    return False
            elif KeyStroke == myCommand.Down:
                if Pumba.pY < 570:
                    newY = Pumba.pY + 40
                    if (newX, newY) not in self.Walls:
                        Pumba.updatePosition(newX, newY)
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False

    def enemyMove(self):
        while True:
            try:
                value = randint(0, 3)
                value2 = randint(1, 15)
                if value == 0:
                    for x in range(value2):
                        if self.tryMoveTimon(self.EnemyTimon, myCommand.Right):
                            time.sleep(self.EnemyTimon.Speed)
                if value == 1:
                    for x in range(value2):
                        if self.tryMoveTimon(self.EnemyTimon, myCommand.Left):
                            time.sleep(self.EnemyTimon.Speed)
                if value == 2:
                    for x in range(value2):
                        if self.tryMoveTimon(self.EnemyTimon, myCommand.Up):
                            time.sleep(self.EnemyTimon.Speed)
                if value == 3:
                    for x in range(value2):
                        if self.tryMoveTimon(self.EnemyTimon, myCommand.Down):
                            time.sleep(self.EnemyTimon.Speed)
            except:
                print("")

    def enemyMove2(self):
        while True:
            try:
                value = randint(0, 3)
                value2 = randint(1, 15)
                if value == 0:
                    for x in range(value2):
                        if self.tryMoveTimon(self.EnemyPumba, myCommand.Right):
                            time.sleep(self.EnemyPumba.Speed)
                if value == 1:
                    for x in range(value2):
                        if self.tryMoveTimon(self.EnemyPumba, myCommand.Left):
                            time.sleep(self.EnemyPumba.Speed)
                if value == 2:
                    for x in range(value2):
                        if self.tryMoveTimon(self.EnemyPumba, myCommand.Up):
                            time.sleep(self.EnemyPumba.Speed)
                if value == 3:
                    for x in range(value2):
                        if self.tryMoveTimon(self.EnemyPumba, myCommand.Down):
                            time.sleep(self.EnemyPumba.Speed)
            except:
                print("")


    def keyEvent2(self):
        while True:
            try:
                if keyboard.is_pressed('a'):
                    self.tryMove(self.PlayerDict[1], myCommand.Left)
                elif keyboard.is_pressed('d'):
                    self.tryMove(self.PlayerDict[1], myCommand.Right)
                elif keyboard.is_pressed('w'):
                    self.tryMove(self.PlayerDict[1], myCommand.Up)
                elif keyboard.is_pressed('s'):
                    self.tryMove(self.PlayerDict[1], myCommand.Down)
            except:
                print('')
            time.sleep(0.1)


    def keyEvent(self):
        while True:
            try:
                if keyboard.is_pressed('left'):
                    self.tryMove(self.PlayerDict[0], myCommand.Left)
                elif keyboard.is_pressed('right'):
                    self.tryMove(self.PlayerDict[0], myCommand.Right)
                elif keyboard.is_pressed('up'):
                    self.tryMove(self.PlayerDict[0], myCommand.Up)
                elif keyboard.is_pressed('down'):
                    self.tryMove(self.PlayerDict[0], myCommand.Down)
                elif keyboard.is_pressed('escape'):
                    self.close()
            except:
                print('')
            time.sleep(0.1)


    def tryMove(self, Player, KeyStroke):
        newX = Player.pX
        newY = Player.pY
        PixmapFoot = QPixmap(Player.PictureFoot)
        PixmapResizedFoot = PixmapFoot.scaled(40, 40)
        if Player.CanMove == True:
            if KeyStroke == myCommand.Left:
                if Player.pX> 10:
                     newX = Player.pX - 40
                     if(newX,newY) not in self.Walls:
                         Player.updatePosition(newX, newY)
                         if (newX, newY) in self.Space:
                             self.FootLabel.setPixmap(PixmapResizedFoot)
                             self.FootLabel.move(newX, newY)
                             self.Space.remove((newX, newY))
            elif KeyStroke == myCommand.Right:
                if Player.pX < 770:
                     newX = Player.pX + 40
                     if (newX, newY) not in self.Walls:
                        Player.updatePosition(newX, newY)
                        if (newX, newY) in self.Space:
                            self.FootLabel.setPixmap(PixmapResizedFoot)
                            self.FootLabel.move(newX, newY)
                            self.Space.remove((newX, newY))
            elif KeyStroke == myCommand.Up:
                if Player.pY >10:
                     newY = Player.pY - 40
                     if (newX, newY) not in self.Walls:
                         Player.updatePosition(newX, newY)
                         if (newX, newY) in self.Space:
                             self.FootLabel.setPixmap(PixmapResizedFoot)
                             self.FootLabel.move(newX, newY)
                             self.Space.remove((newX, newY))
            elif KeyStroke == myCommand.Down:
                if Player.pY < 570:
                     newY = Player.pY + 40
                     if (newX, newY) not in self.Walls:
                         Player.updatePosition(newX, newY)
                         if (newX, newY) in self.Space:
                             self.FootLabel.setPixmap(PixmapResizedFoot)
                             self.FootLabel.move(newX, newY)
                             self.Space.remove((newX, newY))


    def playerDead(self):
        while True:
            if self.EnemyPumba.pX == self.PlayerDict[1].pX and self.EnemyPumba.pY == self.PlayerDict[1].pY:
                self.PlayerDict[1].updatePosition(10, 570)
            if self.EnemyPumba.pX == self.PlayerDict[0].pX and self.EnemyPumba.pY == self.PlayerDict[0].pY:
                self.PlayerDict[0].updatePosition(770, 570)
            if self.EnemyTimon.pX == self.PlayerDict[1].pX and self.EnemyTimon.pY == self.PlayerDict[1].pY:
                self.PlayerDict[1].updatePosition(10, 570)
            if self.EnemyTimon.pX == self.PlayerDict[0].pX and self.EnemyTimon.pY == self.PlayerDict[0].pY:
                self.PlayerDict[0].updatePosition(770, 570)
            time.sleep(0.1)

    def createLabels(self):

        self.FootLabel = QLabel(self)
        self.FootLabel2 = QLabel(self)

    def createLabel(self, newx, newy):
        self.FootLabel = QLabel(self)
        self.FootLabel2 = QLabel(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = LavirintP()
    sys.exit(app.exec_())