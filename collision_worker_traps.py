import time

from worker import Worker
import multiprocessing as mp


class CollisionWorkerTrap(Worker):

    def __init__(self, players, traps, in_q: mp.Queue, out_q: mp.Queue):
        super().__init__()
        self.traps = traps
        self.players = players
        self.i_p = in_q
        self.o_p = out_q

    def work(self):
        while True:
            trps = list(map(lambda x: [x.pX, x.pY, x.ID], self.traps))
            ply = list(map(lambda x: [x.pX, x.pY], self.players))

            self.i_p.put([ply, trps])
            val = self.o_p.get()
            #print(val)
            if val != -1:
                for p in range(len(self.traps)):

                    if(self.traps[p].ID == val):
                        #print(self.traps[p].ID)
                        self.traps[p].activeTrap.emit()
                        #print(p)

                        #self.update.emit()
                while not self.o_p.empty():
                    self.o_p.get()

           # print("*")
            time.sleep(0.001)
