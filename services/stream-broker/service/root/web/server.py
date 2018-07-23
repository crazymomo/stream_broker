# ex: et sw=4 ts=4 sts=4

from concurrent import futures

from tornado import ioloop
from tornado import web
from tornado import gen

from root.command.command_center import CommandCenter, HTTP_PATH_NOTIFY, HTTP_PATH_ADD, HTTP_PATH_REMOVE, HTTP_PATH_LIST

from root.stream.stream_center import StreamCenter

from root.util.config import THREAD_COUNT
from root.util.log_util import Logger

class AbstractHandler(web.RequestHandler):
    
    @gen.coroutine
    def get(self):
        # get thread pool
        pool = self.settings['pool']
        # send event to another thread
        yield pool.submit(CommandCenter.getInstance().execute, self)

    @gen.coroutine
    def post(self):
        # get thread pool
        pool = self.settings['pool']
        # send event to another thread
        yield pool.submit(CommandCenter.getInstance().execute, self)
        
class Server(object):
    
    def __init__(self):
        # set logger
        self._logger = Logger('server')
        # init command center
        CommandCenter.getInstance()
        # init stream center
        StreamCenter.getInstance()
    
    def start(self, port):
        try:
            # init pool
            pool = futures.ThreadPoolExecutor(THREAD_COUNT)
            
            # init application
            application = web.Application(
                [
                    (HTTP_PATH_NOTIFY, AbstractHandler),
                    (HTTP_PATH_ADD, AbstractHandler),
                    (HTTP_PATH_REMOVE, AbstractHandler),
                    (HTTP_PATH_LIST, AbstractHandler)
                ],
                pool    = pool,
                debug   = True
            )
            
            # bind server
            application.listen(port)
            
            # start event loop
            ioloop.IOLoop.instance().start()
        except OSError as e:
            self._logger.debug(e)
