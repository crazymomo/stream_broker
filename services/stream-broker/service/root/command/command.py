# ex: et sw=4 ts=4 sts=4

from root.util.config import MODULE_ROOT
from root.util.log_util import Logger

class Command(object):
    
    def __init__(self):
        self._request_list = {}
        self._result_list = {}
        self._logger = Logger("request")
    
    def execute(self, handler):
        print('Run abstract command')
