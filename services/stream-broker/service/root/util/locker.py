# ex: et sw=4 ts=4 sts=4

import threading

class Locker:
    
    def __init__(self, lock):
        self._lock = lock
        self._lock.acquire()

    def __del__(self):
        self._lock.release()