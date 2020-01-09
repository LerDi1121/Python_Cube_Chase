"""vujadin"""
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import *
from Map import *

class Player(QFrame):
        PlayerWidth = 40
        PlayerHeight = 40
        PictureFoot = ""
        pX = 0
        pY = 0
        startX = 0
        startY = 0
        Live = 0
        LabelPlayer = 0
        Picture = ""
        ID = 0
        CanMove = True
        IsAlive = True
        Dead= pyqtSignal()
        up = pyqtSignal()
        down = pyqtSignal()
        left = pyqtSignal()
        right = pyqtSignal()

        def __init__(self, parent, x, y, picture, footPicture, id):
            super().__init__(parent)

            self.initPlayer(parent, x, y, picture, footPicture, id)

        def initPlayer(self, parent, x, y, picture, footPicture, id):
            self.resize(800, 600)
            self.pX = x
            self.pY = y
            self.startX = x
            self.startY = y
            self.Live=3
            self.ID =id
            self.Picture = picture
            self.PictureFoot = footPicture
            self.up.connect(self.move_up)
            self.down.connect(self.move_down)
            self.left.connect(self.move_left)
            self.right.connect(self.move_right)
            self.Dead.connect(self.deadPlayer)
            self.LabelPlayer = QLabel(parent)
            PixmapPlayer = QPixmap(picture)
            PixmapResizedPlayer = PixmapPlayer.scaled(self.PlayerWidth, self.PlayerHeight)
            self.LabelPlayer.setPixmap(PixmapResizedPlayer)
            self.LabelPlayer.move(x, y)

        def updatePosition(self, x, y):
            self.pX = x
            self.pY = y
            PixmapPlayer = QPixmap(self.Picture)
            PixmapResizedPlayer = PixmapPlayer.scaled(self.PlayerWidth, self.PlayerHeight)
            self.LabelPlayer.setPixmap(PixmapResizedPlayer)
            self.LabelPlayer.move(x, y)

        def deadPlayer(self):
            if(self.Live - 1) >= 0:
                self.Live = self.Live - 1
                self.updatePosition(self.startX, self.startY)
                print("Nesto se desilo")

        def move_up(self):
            if self.CanMove == True:
                newX = self.pX
                newY = self.pY
                if self.pY > 10:
                    newY = self.pY - 40
                    if (newX, newY) not in Map.Walls:
                        self.updatePosition(newX, newY)
                        self.update()
                        #if (newX, newY) in Map.Space:
                      #      PixmapFoot = QPixmap(self.PictureFoot)
                       #     PixmapResizedFoot = PixmapFoot.scaled(40, 40)
                        #    self.FootLabel.setPixmap(PixmapResizedFoot)
                        #    self.FootLabel.move(newX, newY)
                         #   self.Space.remove((newX, newY))

        def move_down(self):
            if self.CanMove == True:
                newX = self.pX
                newY = self.pY
                if self.pY< 570:
                    newY = self.pY + 40
                    if (newX, newY) not in Map.Walls:
                        self.updatePosition(newX, newY)
                        self.update()
                       # if (newX, newY) in self.Space:
                        #    PixmapFoot = QPixmap(self.PictureFoot)
                         #   PixmapResizedFoot = PixmapFoot.scaled(40, 40)
                          #  self.FootLabel.setPixmap(PixmapResizedFoot)
                           # self.FootLabel.move(newX, newY)
                            #self.Space.remove((newX, newY))

        def move_right(self):
            if self.CanMove == True:
                newX = self.pX
                newY = self.pY
                if self.pX  < 770:
                    newX = self.pX + 40
                    if (newX, newY) not in Map.Walls:
                        self.updatePosition(newX, newY)
                        self.update()
                     #   if (newX, newY) in self.Space:
                     #       PixmapFoot = QPixmap(self.PictureFoot)
                     #       PixmapResizedFoot = PixmapFoot.scaled(40, 40)
                     #       self.FootLabel.setPixmap(PixmapResizedFoot)
                     #       self.FootLabel.move(newX, newY)
                     #       self.Space.remove((newX, newY))


        def move_left(self):
            if self.CanMove == True:
                newX = self.pX
                newY = self.pY
                if self.pX  > 10:
                    newX = self.pX - 40
                    if (newX, newY) not in Map.Walls:
                        self.updatePosition(newX, newY)
                        self.update()
                     #   if (newX, newY) in self.Space:
                     #       PixmapFoot = QPixmap(self.PictureFoot)
                     #       PixmapResizedFoot = PixmapFoot.scaled(40, 40)
                     #       self.FootLabel.setPixmap(PixmapResizedFoot)
                     #       self.FootLabel.move(newX, newY)
                     #       self.Space.remove((newX, newY))



