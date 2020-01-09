from random import randint

from PyQt5.QtWidgets import QMainWindow, QGridLayout, QFrame, QDesktopWidget, QApplication, QWidget, QHBoxLayout, QLabel, QFileDialog
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, QTimerEvent
from PyQt5.QtGui import *
from Player  import *
from collision_proces import *
from collision_worker import *
from multiprocessing import Queue
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


        super(LavirintP, self).__init__()
        self.InitStart()
        self.PlayerDict = {}
        self.EnemyDict={}
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

        Walls = []
        Grass = []
        Space = []
        UseSpace = []
        map = Map()
        map.wall()


        self.in_queue = Queue()
        self.out_queue = Queue()
        self.playerProcess = CollisionProcess(self.in_queue, self.out_queue)
        self.playerProcess.start()
        self.playerCollisionWorker = CollisionWorker(self.PlayerDict, self.EnemyDict, self.in_queue,self.out_queue)
        self.playerCollisionWorker.update.connect(self.close_app)
        self.playerCollisionWorker.start()
        self.show()
        T3=Thread(target=self.enemyMove)
        T3.daemon = True
      #  T3.start()
        # KeyPressThread"""
        T4=Thread(target=self.enemyMove2)
        T4.daemon = True
       # T4.start()
        # KeyPressThread"""
      #  T5 = Thread(target=self.playerDead)
       # T5.daemon = True
       # T5.start()
        # KeyPressThread"""


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

    def createPlayerAndEnemy(self):

        self.PlayerDict[0] = Player(self, 770, 570, 'images\Simba.png', 'images\imgfoot1_small.png', 0)
        self.PlayerDict[1] = Player(self, 10, 570, 'images\imgNala.png', 'images\imgfoot2_small.png',  1)
        self.EnemyDict[1] = Enemy(self, 10, 10, 'images\imgTimon.png',0)
        self.EnemyDict[0] = Enemy(self, 770, 10, 'images\pumba.png',1)


    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def timerEvent(self, a0: 'QTimerEvent'):
        self.EnemyDict[1].move.emit()
        self.EnemyDict[0].move.emit()
        #time.sleep(self.EnemyDict[0].Speed)

    def tryMoveEnemy(self, Enemy, KeyStroke):
        newX = Enemy.pX
        newY = Enemy.pY

        if Enemy.CanMove == True:
            if KeyStroke == myCommand.Left:
                if Enemy.pX> 10:
                     newX = Enemy.pX - 40
                     if(newX,newY) not in Map.Walls:
                         Enemy.updatePosition(newX, newY)
                         return True
                     else:
                         return False
                else:
                    return False
            elif KeyStroke == myCommand.Right:
                if Enemy.pX <770:
                     newX = Enemy.pX + 40
                     if (newX, newY) not in Map.Walls:
                        Enemy.updatePosition(newX, newY)
                        return True
                     else:
                        return False
                else:
                    return False
            elif KeyStroke == myCommand.Up:
                if Enemy.pY >10:
                     newY = Enemy.pY - 40
                     if (newX, newY) not in Map.Walls:
                         Enemy.updatePosition(newX, newY)
                         return True
                     else:
                         return False
                else:
                    return False
            elif KeyStroke == myCommand.Down:
                if Enemy.pY < 570:
                     newY = Enemy.pY + 40
                     if (newX, newY) not in Map.Walls:
                         Enemy.updatePosition(newX, newY)
                         return True
                     else:
                         return False
                else:
                    return False
        else:
            return False


    def enemyMove(self):
        Enemy = self.EnemyDict[0]
        while True:
            try:
                value = randint(0, 3)
                value2 = randint(1, 15)
                if value == 0:
                    for x in range(value2):
                        if self.tryMoveEnemy(Enemy, myCommand.Right):
                            time.sleep(Enemy.Speed)
                if value == 1:
                    for x in range(value2):
                        if self.tryMoveEnemy(Enemy, myCommand.Left):
                            time.sleep(Enemy.Speed)
                if value == 2:
                    for x in range(value2):
                        if self.tryMoveEnemy(Enemy, myCommand.Up):
                            time.sleep(Enemy.Speed)
                if value == 3:
                    for x in range(value2):
                        if self.tryMoveEnemy(Enemy, myCommand.Down):
                            time.sleep(Enemy.Speed)
            except:
                pom=3

    def enemyMove2(self):
        Enemy = self.EnemyDict[1]
        while True:
            try:
                value = randint(0, 3)
                value2 = randint(1, 15)
                if value == 0:
                    for x in range(value2):
                        if self.tryMoveEnemy(Enemy, myCommand.Right):
                            time.sleep(Enemy.Speed)
                if value == 1:
                    for x in range(value2):
                        if self.tryMoveEnemy(Enemy, myCommand.Left):
                            time.sleep(Enemy.Speed)
                if value == 2:
                    for x in range(value2):
                        if self.tryMoveEnemy(Enemy, myCommand.Up):
                            time.sleep(Enemy.Speed)
                if value == 3:
                    for x in range(value2):
                        if self.tryMoveEnemy(Enemy, myCommand.Down):
                            time.sleep(Enemy.Speed)
            except:
                pom=3



    def close_app(self):
        self.close_all_proccesses_threads()
        #QMessageBox.question(self, 'Game', "Game Over", QMessageBox.Ok)
        self.close()

    def closeEvent(self, a0: QCloseEvent):
        self.close_all_proccesses_threads()


        self.CollisionWorker.thread.terminate()
        self.playerProcess.terminate()
        self.bulletCollisionWorker.thread.terminate()
        self.bulletProcess.terminate()



    def keyPressEvent(self, e : QKeyEvent):
        if e.key() == Qt.Key_Up:
            self.PlayerDict[0].up.emit()
        elif e.key() == Qt.Key_Down:
            self.PlayerDict[0].down.emit()
        elif e.key() == Qt.Key_Left:
            self.PlayerDict[0].left.emit()
        elif e.key() == Qt.Key_Right:
            self.PlayerDict[0].right.emit()
        elif e.key()==Qt.Key_W:
            self.PlayerDict[1].up.emit()
        elif e.key() == Qt.Key_S:
            self.PlayerDict[1].down.emit()
        elif e.key()==Qt.Key_D:
            self.PlayerDict[1].right.emit()
        elif e.key() == Qt.Key_A:
            self.PlayerDict[1].left.emit()


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