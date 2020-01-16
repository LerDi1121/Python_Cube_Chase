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
            enem = list(map(lambda x: [x.pX, x.pY, x.CanMove], self.enemies)) #za svako x (sve u enemy) uzmi px py i can move(parametre)
            ply = list(map(lambda x: [x.pX, x.pY, x.ID], self.players))  #isto i ovde

            self.i_p.put([ply, enem]) #stavlja to od gore tu
            val = self.o_p.get()  #vraca id igraca

            if val != -1:
                for p in range(len(self.players)):
                    if(self.players[p].ID == val):  #ako je plejer sa tim idjom i ubija ga ako je taj id
                        self.players[p].Dead.emit()


                        #self.update.emit()
                while not self.o_p.empty():
                    self.o_p.get()


            time.sleep(0.001)
