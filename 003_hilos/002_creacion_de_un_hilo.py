import threading
import time


class MiHilo(threading.Thread):
    def run(self):
        print("{} Inició".format(self.name))
        time.sleep(1)
        print("{} terminado".format(self.name))

if __name__=="__main__":
    for x in range(4):
        hilo = MiHilo(name="Thread-{}".format(x+1))
        hilo.start()
        time.sleep(.5)