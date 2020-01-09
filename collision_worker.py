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
            val = self.o_p.get()
            print(val)
            if val != -1:
                for player in self.players:
                    if player.ID == val:
                        player.Dead()

                        self.update.emit()
                        return
            time.sleep(0.01)
