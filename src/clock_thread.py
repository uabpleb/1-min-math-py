
import threading
import time


class ClockThread(threading.Thread):
    def __init__(self, duration):
        threading.Thread.__init__(self)
        self.duration = duration
        self.finished = False

    def run(self):
        print("starting clock...")
        time.sleep(self.duration)
        self.finished = True
        print("finished clock.")

    def done(self)->bool:
        return self.finished
