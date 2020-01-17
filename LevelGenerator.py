from Player  import *
from TrapAndForce import TrapAndForce
from collision_proccess_trap_enemy import CollisionProcessTrapEnemy
from collision_proces import *
from collision_process_trap import CollisionProcessTrap
from collision_worker import *
from multiprocessing import Queue
from Pumba import *
from threading import Thread

import sys

from Map import *
from collision_worker_trap_enemy import CollisionWorkerTrapEnemy
from collision_worker_traps import CollisionWorkerTrap


class LavirintP(QMainWindow):

    def __init__(self, mainWind):

        super(LavirintP, self).__init__()
        self.InitStart()
        self.MainWind= mainWind
        self.PlayerDict = []
        self.EnemyDict = []
        self.Traps = []
        self.defTraps()
        self.createPlayerAndEnemy()
        self.lblPly1Score = QLabel(self)
        self.GameOver = QLabel(self)
        self.lblPly2Score = QLabel(self)
        self.Lvlcounter = 1
        self.LevelLbl = QLabel(self)
        self.lblScore()
        self.map = Map()
        self.map.wall()
        self.force = TrapAndForce(self, 1, 2)

        self.in_queue = Queue() #za koliziju igraca i neprijatelja
        self.out_queue = Queue()
        self.in_queue_trap = Queue() #za koliziju za aktiviranje zamke (kad igrac predje preko zamke)
        self.out_queue_trap = Queue()
        self.in_queue_trap_enemy = Queue() #za koliziju kad neprijatelj predje preko zamke
        self.out_queue_trap_enemy = Queue()

        #enemy and ply
        self.playerProcess = CollisionProcess(self.in_queue, self.out_queue)
        self.playerProcess.start()
        self.playerCollisionWorker = CollisionWorker(self.PlayerDict, self.EnemyDict, self.in_queue,self.out_queue)
        self.playerCollisionWorker.update.connect(self.close_app)
        self.playerCollisionWorker.start()

        #ply and traps
        self.TrapEnemyProcess = CollisionProcessTrap(self.in_queue_trap, self.out_queue_trap)
        self.TrapEnemyProcess.start()
        self.TrapEnemyCollisionWorker = CollisionWorkerTrap(self.PlayerDict, self.Traps, self.in_queue_trap, self.out_queue_trap)
        self.TrapEnemyCollisionWorker.update.connect(self.close_app)
        self.TrapEnemyCollisionWorker.start()

        # enemy and traps
        self.TrapActiveProcess = CollisionProcessTrapEnemy(self.in_queue_trap_enemy, self.out_queue_trap_enemy)
        self.TrapActiveProcess.start()
        self.TrapActiveCollisionWorker = CollisionWorkerTrapEnemy(self.EnemyDict, self.Traps, self.in_queue_trap_enemy, self.out_queue_trap_enemy)
        self.TrapActiveCollisionWorker.update.connect(self.close_app)
        self.TrapActiveCollisionWorker.start()

        self.timer = QBasicTimer()
        self.timer.start(30, self)

        self.thread1 = Thread(target=self.EnemyDict[0].changeCoord)
        self.thread1.daemon = True
        self.thread1.start()
        self.thread2 = Thread(target=self.EnemyDict[1].changeCoord)
        self.thread2.daemon = True
        self.thread2.start()
        self.thread3 = Thread(target=self.level)
        self.thread3.daemon = True
        self.thread3.start()

        self.threadForce = Thread(target=self.ForceLogic)
        self.threadForce.daemon = True
        self.threadForce.start()

        self.UsedSpace = []
        self.show()


    def defTraps(self):

        self.Traps.append(TrapAndForce(self, 1, 1))
        self.Traps.append(TrapAndForce(self, 2, 1))
        self.Traps.append(TrapAndForce(self, 3, 1))
        self.Traps.append(TrapAndForce(self, 4, 1))
        self.Traps.append(TrapAndForce(self, 5, 1))


    def lblScore(self):
        self.lblPly1Score.move(565, 620)
        self.lblPly1Score.resize(250, 60)
        self.lblPly1Score.setFrameStyle(3)
        self.setStyleSheet("QLabel {font: 15pt Comic Sans MS}")

        self.lblPly2Score.move(5, 620)
        self.lblPly2Score.resize(250, 60)
        self.lblPly2Score.setFrameStyle(3)
        self.LevelLbl.move(370, 620)

        self.LevelLbl.resize(100, 60)
        self.LevelLbl.setFrameStyle(3)
        self.LevelLbl.setText("Level :" + str(self.Lvlcounter))


    def ForceLogic(self):
        while True:
            self.force.activeForce()
            time.sleep(5)
            #provera sa poklapanjem koordinata
            for i in range(len(self.PlayerDict)):
                if self.force.pX == self.PlayerDict[i].pX and self.force.pY == self.PlayerDict[i].pY:
                    forceInt = randint(0, 200)
                    if forceInt % 2 == 0:
                        self.PlayerDict[i].Live = self.PlayerDict[i].Live + 1
                    else:
                        self.PlayerDict[i].Score = self.PlayerDict[i].Score - 1234

            self.force.deactiveForce()
            time.sleep(5)

    def level(self):
        while True:
            if Map.Counter==0:
                self.newLevel()
            if self.PlayerDict[0].Live==0 or self.PlayerDict[1].Live==0:
                self.gameOver()

            time.sleep(0.2)

    def gameOver(self):
        if self.PlayerDict[0].Live == 0:
            self.GameOver.setText("Player 2 wins!!!")
        elif self.PlayerDict[1].Live == 0:
            self.GameOver.setText("Player 1 wins!!!")
        else:
            if  self.PlayerDict[0].Score< self.PlayerDict[1].Score:
                self.GameOver.setText("Player 2 wins!!!")
            else:
                self.GameOver.setText("Player 1 wins!!!")
        self.GameOver.resize(350, 60)
        self.GameOver.move(235, 100)
        self.GameOver.setStyleSheet("font: 40pt Comic Sans MS; color: red")
        time.sleep(5)
        self.MainWind.show()
        self.close_app()
        app = QApplication.instance()
        # app.quit()

    def newLevel(self):
        if self.Lvlcounter <6:
            if self.PlayerDict[0] != None:
                self.PlayerDict[0].newLvl.emit()
            if self.PlayerDict[1] != None:
                self.PlayerDict[1].newLvl.emit()
            self.defTraps()
            self.EnemyDict[0].Speed=self.EnemyDict[0].Speed - 0.05
            self.EnemyDict[1].Speed=self.EnemyDict[1].Speed - 0.05
            if self.EnemyDict[0].Speed<0:
                self.gameOver()

            self.map.wall()
            self.Lvlcounter= self.Lvlcounter + 1
            self.LevelLbl.setText("Level :" + str(self.Lvlcounter))
            time.sleep(1)
        else:
            self.gameOver()

    def timerEvent(self, event):
        if self.PlayerDict[0] != None:
            self.lblPly1Score.setText("Player 1:" + str(self.PlayerDict[0].Score)+ " Lives: " + str(self.PlayerDict[0].Live))
        if self.PlayerDict[1] != None:
            self.lblPly2Score.setText("Player 2:" + str(self.PlayerDict[1].Score) + " Lives: " + str(self.PlayerDict[1].Live))

    def InitStart(self):
        self.resize(820, 680)
        self.center()
        self.setWindowTitle("Cub Chase")
        self.center()
        hbox = QHBoxLayout(self)
        pixmap = QPixmap('images\imgBackground2.png')
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        QLabel.setGeometry(lbl, 0, 0, 820, 620)
        hbox.addWidget(lbl)
        self.resize(pixmap.width(), pixmap.height()+60)
        self.setLayout(hbox)

    def createPlayerAndEnemy(self):
        self.PlayerDict.append(Player(self, 770, 570, 'images\Simba.png', 0))
        self.PlayerDict.append(Player(self, 10, 570, 'images\imgNala.png', 1))
        self.EnemyDict.append(Enemy(self, 10, 10, 'images\imgTimon.png',0))
        self.EnemyDict.append(Enemy(self, 770, 10, 'images\pumba.png',1))

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2),int( (screen.height() - size.height()) / 2))

    def close_app(self):
        self.playerCollisionWorker.ind =False
        self.playerCollisionWorker.thread.terminate()
        self.playerProcess.terminate()

        self.TrapActiveCollisionWorker.ind = False
        self.TrapActiveCollisionWorker.thread.terminate()
        self.TrapActiveProcess.terminate()

        self.TrapEnemyCollisionWorker.ind = False
        self.TrapEnemyCollisionWorker.thread.terminate()
        self.TrapEnemyProcess.terminate()
        self.close()

    def keyPressEvent(self, e: QKeyEvent):
        if e.key() == Qt.Key_Up:
            self.PlayerDict[0].up.emit()
            time.sleep(0.05)
        if e.key() == Qt.Key_Down:
            self.PlayerDict[0].down.emit()
            time.sleep(0.05)
        if e.key() == Qt.Key_Left:
            self.PlayerDict[0].left.emit()
            time.sleep(0.05)
        if e.key() == Qt.Key_Right:
            self.PlayerDict[0].right.emit()
            time.sleep(0.05)
        if e.key()==Qt.Key_W:
            self.PlayerDict[1].up.emit()
            time.sleep(0.05)
        if e.key() == Qt.Key_S:
            self.PlayerDict[1].down.emit()
            time.sleep(0.05)
        if e.key()==Qt.Key_D:
            self.PlayerDict[1].right.emit()
            time.sleep(0.05)
        if e.key() == Qt.Key_A:
            self.PlayerDict[1].left.emit()
            time.sleep(0.05)
        if e.key() == Qt.Key_Escape:
            self.close_app()
