from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QWidget, QHBoxLayout, QLabel, QFileDialog
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

import multiprocessing as mp

from PyQt5.uic.properties import QtGui


class LavirintP(QMainWindow):
    def __init__(self):
        self.Walls=[]
        self.Grass=[]
        super(LavirintP, self).__init__()
        self.InitStart()
        self.PlayerDist = {}
        self.EnemyPumba = None
        self.EnemyTimon = None
        self.createPlayerAndEnemy()
        Thread(target=self.keyEvent).start()    #KeyPressThread
        Thread(target=self.keyEvent2).start()    #KeyPressThread

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

        self.PlayerDist[0] = Player(self, 770, 570, 'images\Simba.png', 0)
        self.PlayerDist[1] = Player(self, 10, 570, 'images\imgNala.png', 1)
        self.EnemyTimon = Timon(self, 210, 100, 'images\imgTimon.png')
        self.EnemyPumba = Pumba(self, 210, 200, 'images\pumba.png')

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


    def wall(self):
        for x in range (len( Map.Level)):
            for y in range(len(Map.Level[x])):
                character = Map.Level[x][y]
                if character =="X":
                    coordX = x * 40 + 10
                    coordY = y * 40 + 10
                    self.Walls.append((coordY, coordX))
                if character=="G":
                    coordX = x * 40 + 10
                    coordY = y * 40 + 10
                    self.Grass.append((coordY, coordX))
        print(self.Walls)


    def keyEvent2(self):
        while True:
            try:
                if keyboard.is_pressed('a'):
                    self.tryMove(self.PlayerDist[1], myCommand.Left)
                elif keyboard.is_pressed('d'):
                    self.tryMove(self.PlayerDist[1], myCommand.Right)
                elif keyboard.is_pressed('w'):
                    self.tryMove(self.PlayerDist[1], myCommand.Up)
                elif keyboard.is_pressed('s'):
                    self.tryMove(self.PlayerDist[1], myCommand.Down)
            except:
                print('Neko drugo dugme...')
            time.sleep(0.1)


    def keyEvent(self):
        while True:
            try:
                if keyboard.is_pressed('left'):
                    self.tryMove(self.PlayerDist[0], myCommand.Left)
                elif keyboard.is_pressed('right'):
                    self.tryMove(self.PlayerDist[0], myCommand.Right)
                elif keyboard.is_pressed('up'):
                    self.tryMove(self.PlayerDist[0], myCommand.Up)
                elif keyboard.is_pressed('down'):
                    self.tryMove(self.PlayerDist[0], myCommand.Down)
                elif keyboard.is_pressed('escape'):
                    self.close()
            except:
                print('Neko drugo dugme...')
            time.sleep(0.1)


    def tryMove(self, Player, KeyStroke):
        newX = Player.pX
        newY = Player.pY

        if Player.CanMove == True:
            if KeyStroke == myCommand.Left:
                if Player.pX> 10:
                     newX = Player.pX - 40
                     if(newX,newY) not in self.Walls:
                         Player.updatePosition(newX, newY)
            elif KeyStroke == myCommand.Right:
                if Player.pX <770:
                     newX = Player.pX + 40
                     if (newX, newY) not in self.Walls:
                        Player.updatePosition(newX, newY)
            elif KeyStroke == myCommand.Up:
                if Player.pY >10:
                     newY = Player.pY - 40
                     if (newX, newY) not in self.Walls:
                         Player.updatePosition(newX, newY)
            elif KeyStroke == myCommand.Down:
                if Player.pY < 570:
                     newY = Player.pY + 40
                     if (newX, newY) not in self.Walls:
                         Player.updatePosition(newX, newY)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = LavirintP()
    sys.exit(app.exec_())