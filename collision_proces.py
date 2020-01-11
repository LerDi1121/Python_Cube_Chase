import math
import time
import multiprocessing as mp


from Pumba import Enemy

class CollisionProcess(mp.Process):

    def __init__(self, in_q : mp.Queue,out_q : mp.Queue, ):
        super().__init__(target=self.__work__, args=[in_q, out_q])

    def __work__(self, in_q: mp.Queue, out_q: mp.Queue ):

        while True:
            temp= False
            while not in_q.empty():
                tp = in_q.get()

            enemies = tp[1]
            players = tp[0]
            for e in range(len(enemies)):
                for p in range(len(players)):
                    if enemies[e][1] == players[p][1] and enemies[e][0] == players[p][0]:
                        out_q.put(players[p][2])
                        temp = True
                        time.sleep(0.1)
                        break
                if temp:
                    time.sleep(0.1)
                    break

            time.sleep(0.01)
            out_q.put(-1)
