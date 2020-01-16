import time

from worker import Worker
import multiprocessing as mp


class CollisionWorkerTrapEnemy(Worker):

    def __init__(self, enemys, traps, in_q: mp.Queue, out_q: mp.Queue):
        super().__init__()
        self.traps = traps
        self.enemys = enemys
        self.i_p = in_q
        self.o_p = out_q

    def work(self): #kad neprijatelj stane na zamku
        while True:
            trps = list(map(lambda x: [x.pX, x.pY, x.ID, x.isActive], self.traps))
            enm = list(map(lambda x: [x.pX, x.pY,x.ID], self.enemys))

            self.i_p.put([enm, trps])
            val = self.o_p.get()

            if val != -1:
                for p in range(len(self.enemys)):
                    if(self.enemys[p].ID == val[1]):
                        self.enemys[p].inTrap.emit()

                for p in range(len(self.traps)):
                    if (self.traps[p].ID == val[0]):
                        self.traps[p].deactiveTrap.emit()

                while not self.o_p.empty():
                    self.o_p.get()

           # print("*")
            time.sleep(0.001)
