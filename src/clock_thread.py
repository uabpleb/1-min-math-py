from threading import Thread, Event
import time


class ClockThread(Thread):
    WATCH_INTERVAL = 1

    def __init__(self, duration):
        Thread.__init__(self)
        self.duration = float(duration)
        self.start_time = time.time()

    def run(self):
        print("starting clock...")
        while not self.done():
            time.sleep(self.WATCH_INTERVAL)
            
        #send event

        print("finished clock.")

    def remaining(self):
        return abs(round(self.start_time + self.duration - time.time()))

    def done(self)->bool:
        return time.time() >= self.start_time + self.duration