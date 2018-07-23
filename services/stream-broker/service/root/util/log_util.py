import os
import sys
import logging
import logging.handlers

from .config import LOG_DIR, DAEMON_LOG_PATH

class Logger(object):

    def __init__(self, id_):
        self._logger = logging.getLogger('logger')
        self._id = id_

    def debug(self, msg):
        self._logger.debug(msg, extra={
            'id': self._id,
        })

    def info(self, msg):
        self._logger.info(msg, extra={
            'id': self._id,
        })

    def warning(self, msg):
        self._logger.warning(msg, extra={
            'id': self._id,
        })

    def error(self, msg):
        self._logger.error(msg, extra={
            'id': self._id,
        })

    def exception(self, msg):
        self._logger.exception(msg, extra={
            'id': self._id,
        })

def setup_logger():
    # get logger
    logger = logging.getLogger('logger')
    # disable logger
    logger.propagate = False
    # enable all level from source
    logger.setLevel(logging.DEBUG)
    # log format
    formater = logging.Formatter("%(asctime)s|%(id)s|%(levelname)s|%(threadName)s\t%(message)s")
    
    # setup stdout sink
    handler = logging.StreamHandler()
    handler.setFormatter(formater)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    # setup debug file handler, daily rotate
    if not os.path.isdir(LOG_DIR):
        os.mkdir(LOG_DIR)
    handler = logging.handlers.TimedRotatingFileHandler(DAEMON_LOG_PATH, when='d')
    handler.setFormatter(formater)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
