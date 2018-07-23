# ex: et sw=4 ts=4 sts=4

import re
import shlex
import threading

from tornado.gen import Task, coroutine
from tornado.ioloop import IOLoop, PeriodicCallback
from tornado.process import Subprocess

from root.base.singleton import Singleton

from root.util.locker import Locker
from root.util.system_util import system
from root.util.log_util import Logger

class Stream(threading.Thread):

    def __init__(self, stream_ip, stream_name):
        super().__init__()
        # set ip and name
        self._ip = stream_ip
        self._name = stream_name
        # set logger
        self._logger = Logger('stream')
        # event loop
        self._loop = IOLoop()

    def run(self):
        # queue main action
        self._loop.add_callback(self._once)
        # start event loop in this thread
        self._loop.start()
        # free all resources
        self._loop.close()

    @coroutine
    def stop(self):
        ok = yield Task(lambda callback: self._loop.add_callback(self._stop_, callback))
        return ok

    def _once(self):
        # read and then write rtmp stream (for hls feature)
        cmd = 'ffmpeg -i rtmp://{0}/src/{1} -c:a aac -b:a 64k -c:v libx264 -b:v 256k -vf scale=-1:480 -f flv rtmp://{0}/hls/{1}_480p -c:a aac -b:a 128k -c:v libx264 -b:v 512K -vf scale=-1:720 -f flv rtmp://{0}/hls/{1}_720p' . format(self._ip, self._name)
        self._child = Subprocess(shlex.split(cmd), stdout=Subprocess.STREAM, stderr=Subprocess.STREAM)
        # stop loop
        self._loop.stop()

    def _stop(self):
        try:
            pid = self._child.proc.pid
            self._logger.debug('_stop')
            os.kill(pid, signal.SIGTERM)
        except ProcessLookupError as e:
            self._logger.exception('error on killing pid {0}' . format(pid))

@Singleton
class StreamCenter:
    
    def __init__(self):
        # set lock
        self._lock = threading.Lock()
        # set logger
        self._logger = Logger("stream_center")
    
    def add(self, stream_ip, stream_name):
        #self._stream = Stream(stream_ip, stream_name)
        #self._stream.daemon = True;
        #self._stream.start();
        pass

    def remove(self, stream_ip, stream_name):
        #self._stream.stop();
        pass

    def list(self):
        pass
