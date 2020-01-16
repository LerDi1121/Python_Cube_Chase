import math
import time
import multiprocessing as mp


from Pumba import Enemy

class CollisionProcessTrapEnemy(mp.Process):

    def __init__(self, in_q : mp.Queue,out_q : mp.Queue, ):
        super().__init__(target=self.__work__, args=[in_q, out_q])

    def __work__(self, in_q: mp.Queue, out_q: mp.Queue ):

        while True:
            temp= False
            while not in_q.empty():
                tp = in_q.get()

            traps = tp[1]
            enemys = tp[0]
            for e in range(len(traps)):
                for p in range(len(enemys)):
                    if traps[e][1] == enemys[p][1] and traps[e][0] == enemys[p][0]:
                       if traps[e][3]==True:
                                out_q.put((traps[e][2],enemys[p][2]))
                                temp = True
                                time.sleep(0.1)
                                print("upao")
                                break
                if temp:
                    time.sleep(0.1)
                    break

            time.sleep(0.01)
            out_q.put(-1)
