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
        self.PlayerDict = []
        self.EnemyDict=[]
        self.createPlayerAndEnemy()
        self.createLabels()
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

        self.PlayerDict.append( Player(self, 770, 570, 'images\Simba.png', 'images\imgfoot1_small.png', 0))
        self.PlayerDict.append( Player(self, 10, 570, 'images\imgNala.png', 'images\imgfoot2_small.png',  1))
        self.EnemyDict.append(Enemy(self, 10, 10, 'images\imgTimon.png',0))
        self.EnemyDict.append(Enemy(self, 770, 10, 'images\pumba.png',1))
        #self.timer = self.startTimer(self.EnemyDict[0].Speed)


    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    #def timerEvent(self, a0: 'QTimerEvent'):
      #  self.EnemyDict[1].Move.emit()
      #  self.EnemyDict[0].Move.emit()






    def close_app(self):

        #QMessageBox.question(self, 'Game', "Game Over", QMessageBox.Ok)
        self.close()




    def keyPressEvent(self, e : QKeyEvent):
        if e.key() == Qt.Key_Up:
            self.PlayerDict[0].up.emit()
        if e.key() == Qt.Key_Down:
            self.PlayerDict[0].down.emit()
        if e.key() == Qt.Key_Left:
            self.PlayerDict[0].left.emit()
        if e.key() == Qt.Key_Right:
            self.PlayerDict[0].right.emit()
        if e.key()==Qt.Key_W:
            self.PlayerDict[1].up.emit()
        if e.key() == Qt.Key_S:
            self.PlayerDict[1].down.emit()
        if e.key()==Qt.Key_D:
            self.PlayerDict[1].right.emit()
        if e.key() == Qt.Key_A:
            self.PlayerDict[1].left.emit()




    def createLabels(self):

        self.FootLabel = QLabel(self)
        self.FootLabel2 = QLabel(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = LavirintP()
    sys.exit(app.exec_())