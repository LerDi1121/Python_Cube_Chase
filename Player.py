
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import *
from Map import *


class Player(QFrame):
        PlayerWidth = 40
        PlayerHeight = 40
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
        Dead = pyqtSignal()
        up = pyqtSignal()
        down = pyqtSignal()
        left = pyqtSignal()
        right = pyqtSignal()
        newLvl = pyqtSignal()
        Score = 0

        def __init__(self, parent, x, y, picture,  id):
            super().__init__(parent)

            self.initPlayer(parent, x, y, picture,  id)

        def initPlayer(self, parent, x, y, picture,  id):
            self.resize(40, 40)
            self.pX = x
            self.pY = y
            self.startX = x
            self.startY = y
            self.Live = 3
            self.ID = id
            self.Picture = picture

            self.up.connect(self.move_up)
            self.down.connect(self.move_down)
            self.left.connect(self.move_left)
            self.right.connect(self.move_right)
            self.Dead.connect(self.deadPlayer)
            self.newLvl.connect(self.newLevel)
            self.Score = 0
            self.Foots = []

            for x in range(len(Map.Level)):
                for y in range(len(Map.Level[x])):
                    character = Map.Level[x][y]
                    if character == " ":
                         coordX = x * 40 + 10
                         coordY = y * 40 + 10
                         fp = QLabel(parent)
                         PixmapPlayer = QPixmap('images\imgfoo')
                         PixmapResizedPlayer = PixmapPlayer.scaled(self.PlayerWidth, self.PlayerHeight)
                         fp.setPixmap(PixmapResizedPlayer)
                         fp.move(coordY,coordX)
                         self.Foots.append((fp,(coordY,coordX)))

            self.LabelPlayer = QLabel(parent)
            PixmapPlayer = QPixmap(picture)
            PixmapResizedPlayer = PixmapPlayer.scaled(self.PlayerWidth, self.PlayerHeight)
            self.LabelPlayer.setPixmap(PixmapResizedPlayer)
            self.LabelPlayer.move(self.pX, self.pY)

        def updatePosition(self, x, y):
            self.pX = x
            self.pY = y
            self.LabelPlayer.move(x, y)
            self.update()

        def deadPlayer(self):
            if(self.Live - 1) >= 0:
                self.Live = self.Live - 1
                self.pX = self.startX
                self.pY = self.startY
                self.updatePosition(self.startX, self.startY)
                self.Score = self.Score - 150

                if self.Live == 0:
                    self.CanMove = False

            self.update()

        def newLevel(self):
            self.updatePosition(self.startX, self.startY)
            for fp in range(len(self.Foots)):
                PixmapPlayer = QPixmap('images\ivnvnhhm.png')
                PixmapResizedPlayer = PixmapPlayer.scaled(self.PlayerWidth, self.PlayerHeight)
                self.Foots[fp][0].setPixmap(PixmapResizedPlayer)

        def move_up(self):
            if self.CanMove == True:
                newX = self.pX
                newY = self.pY
                if self.pY > 10:
                    newY = self.pY - 40
                    if (newX, newY) not in Map.Walls:
                        self.updatePosition(newX, newY)
                        self.update()
                        if (newX, newY) in Map.Space:
                            Map.Space.remove((newX, newY))
                            Map.Counter = Map.Counter-1
                            self.Score = self.Score+100
                            for fp in range(len(self.Foots)):
                                if self.Foots[fp][1]==(newX,newY):
                                    PixmapPlayer = QPixmap('images\imgfoot1_small.png')
                                    if self.ID == 1:
                                        PixmapPlayer = QPixmap('images\imgfoot2_small.png')
                                    PixmapResizedPlayer = PixmapPlayer.scaled(self.PlayerWidth, self.PlayerHeight)
                                    self.Foots[fp][0].setPixmap(PixmapResizedPlayer)
                                    self.Foots[fp][0].move(newX, newY)
                                    self.updatePosition(newX, newY)

        def move_down(self):
            if self.CanMove == True:
                newX = self.pX
                newY = self.pY
                if self.pY< 570:
                    newY = self.pY + 40
                    if (newX, newY) not in Map.Walls:
                        self.updatePosition(newX, newY)
                        self.update()
                        if (newX, newY) in Map.Space:
                            Map.Space.remove((newX, newY))
                            self.Score = self.Score + 100
                            Map.Counter = Map.Counter - 1
                            for fp in range(len(self.Foots)):
                                if self.Foots[fp][1]==(newX,newY):
                                    PixmapPlayer = QPixmap('images\imgfoot1_small.png')
                                    if self.ID == 1:
                                        PixmapPlayer = QPixmap('images\imgfoot2_small.png')
                                    PixmapResizedPlayer = PixmapPlayer.scaled(self.PlayerWidth, self.PlayerHeight)
                                    self.Foots[fp][0].setPixmap(PixmapResizedPlayer)
                                    self.Foots[fp][0].move(newX, newY)
                                    self.updatePosition(newX, newY)


        def move_right(self):
            if self.CanMove == True:
                newX = self.pX
                newY = self.pY
                if self.pX  < 770:
                    newX = self.pX + 40
                    if (newX, newY) not in Map.Walls:
                        self.updatePosition(newX, newY)
                        self.update()
                        if (newX, newY) in Map.Space:
                            Map.Space.remove((newX, newY))
                            self.Score = self.Score + 100
                            Map.Counter = Map.Counter - 1
                            for fp in range(len(self.Foots)):
                                if self.Foots[fp][1]==(newX,newY):
                                    PixmapPlayer = QPixmap('images\imgfoot1_small.png')
                                    if self.ID==1:
                                        PixmapPlayer = QPixmap('images\imgfoot2_small.png')

                                    PixmapResizedPlayer = PixmapPlayer.scaled(self.PlayerWidth, self.PlayerHeight)
                                    self.Foots[fp][0].setPixmap(PixmapResizedPlayer)
                                    self.Foots[fp][0].move(newX, newY)
                                    self.updatePosition(newX, newY)


        def move_left(self):
            if self.CanMove == True:
                newX = self.pX
                newY = self.pY
                if self.pX  > 10:
                    newX = self.pX - 40
                    if (newX, newY) not in Map.Walls:
                        self.updatePosition(newX, newY)
                        self.update()
                        if (newX, newY) in Map.Space:
                            Map.Space.remove((newX, newY))
                            self.Score = self.Score + 100
                            Map.Counter = Map.Counter - 1
                            for fp in range(len(self.Foots)):
                                if self.Foots[fp][1] == (newX, newY):
                                    PixmapPlayer = QPixmap('images\imgfoot1_small.png')
                                    if self.ID==1:
                                        PixmapPlayer = QPixmap('images\imgfoot2_small.png')
                                    PixmapResizedPlayer = PixmapPlayer.scaled(self.PlayerWidth, self.PlayerHeight)
                                    self.Foots[fp][0].setPixmap(PixmapResizedPlayer)
                                    self.Foots[fp][0].move(newX, newY)
                                    self.updatePosition(newX, newY)



