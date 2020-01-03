import math
import time
import multiprocessing as mp


class CollisionProcess(mp.Process):

    def __init__(self, in_q : mp.Queue,out_q : mp.Queue, ):
        super().__init__(target=self.__work__, args=[in_q, out_q])

    def __work__(self, in_q: mp.Queue,out_q: mp.Queue ):
        while True:
            tp = in_q.get()
            enemies = tp[1]
            players = tp[0]
            for enemy in enemies:
                for player in players:

                    if enemies.pX == player.pX and enemies.pY == player.pY:
                        out_q.put(player.ID)
                        return

            time.sleep(0.01)
            out_q.put(-1)
