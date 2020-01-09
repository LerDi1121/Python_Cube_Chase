import time

from worker import Worker
import multiprocessing as mp


class CollisionWorker(Worker):

    def __init__(self, players, enemies, in_q: mp.Queue, out_q: mp.Queue):
        super().__init__()
        self.enemies = enemies
        self.players = players
        self.i_p = in_q
        self.o_p = out_q

    def work(self):
        while True:
           # enem = list(map(lambda x: [x.pX(), x.pY()], self.enemies))
            ply = map(lambda x: [x.pX(), x.pY(), x.ID()], self.players)

           #self.i_p.put([ply, enem])
            val = self.o_p.get()

            if val != -1:
                #val.Dead.emit()
                self.update.emit()
            time.sleep(0.01)
