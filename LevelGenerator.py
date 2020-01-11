from Player  import *
from collision_proces import *
from collision_worker import *
from multiprocessing import Queue
from Pumba import *
from threading import Thread

import sys

from Map import *

class LavirintP(QMainWindow):

    def __init__(self):


        super(LavirintP, self).__init__()
        self.InitStart()
        self.PlayerDict = []
        self.EnemyDict=[]
        self.createPlayerAndEnemy()
        self.lblPly1Score= QLabel(self)
        self.lblPly2Score = QLabel(self)

        self.lblPly1Score.move(665,620)
        self.lblPly1Score.resize(150,20)
        self.lblPly1Score.setFrameStyle(3)

        self.lblPly2Score.move(5, 620)
        self.lblPly2Score.resize(150, 20)
        self.lblPly2Score.setFrameStyle(3)
        map = Map()
        map.wall()
        self.in_queue = Queue()
        self.out_queue = Queue()
        self.playerProcess = CollisionProcess(self.in_queue, self.out_queue)
        self.playerProcess.start()
        self.playerCollisionWorker = CollisionWorker(self.PlayerDict, self.EnemyDict, self.in_queue,self.out_queue)
        self.playerCollisionWorker.update.connect(self.close_app)
        self.playerCollisionWorker.start()
        self.timer = QBasicTimer()
        self.timer.start(30, self)
        self.thread1 = Thread(target=self.EnemyDict[0].changeCoord)
        self.thread1.daemon = True
        self.thread1.start()
        self.thread2 = Thread(target=self.EnemyDict[1].changeCoord)
        self.thread2.daemon = True
        self.thread2.start()
        self.show()



    def timerEvent(self, event):
        if self.PlayerDict[0] != None:
            self.lblPly1Score.setText("Player 1:" + str(self.PlayerDict[0].Score)+ " Lives: " +str(self.PlayerDict[0].Live))
        if self.PlayerDict[1] != None:
            self.lblPly2Score.setText("Player 2:" + str(self.PlayerDict[1].Score) + " Lives: " +str(self.PlayerDict[1].Live))
    def InitStart(self):
        self.resize(820, 640)
        self.center()
        self.setWindowTitle("Cub Chase")
        self.center()
        hbox = QHBoxLayout(self)

        pixmap = QPixmap('images\imgBackground2.png')
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        QLabel.setGeometry(lbl, 0, 0, 820, 620)
        hbox.addWidget(lbl)
        self.resize(pixmap.width(), pixmap.height()+20)
        self.setLayout(hbox)


    def createPlayerAndEnemy(self):

        self.PlayerDict.append( Player(self, 770, 570, 'images\Simba.png', 'images\imgfoot1_small.png', 0))
        self.PlayerDict.append( Player(self, 10, 570, 'images\imgNala.png', 'images\imgfoot2_small.png',  1))
        self.EnemyDict.append(Enemy(self, 10, 10, 'images\imgTimon.png',0))
        self.EnemyDict.append(Enemy(self, 770, 10, 'images\pumba.png',1))




    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2),int( (screen.height() - size.height()) / 2))


    def close_app(self):

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





