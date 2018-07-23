# ex: et sw=4 ts=4 sts=4

import json

from root.command.command import Command

from root.stream.stream_center import StreamCenter

from root.util.system_util import system
from root.util.config import MODULE_ROOT

class RemoveCommand(Command):
    
    def __init__(self):
        super().__init__()
    
    def execute(self, handler):
        try:
            # get path and split to tokens
            path = handler.request.path
            tokens = path.split('/')

            # get stream name
            try:
                stream_name = tokens[2]
            except IndexError as e:  
                stream_name = None;

            # remove from stream center
            StreamCenter.getInstance().remove(stream_name)
        except Exception as e:
            self._logger.debug(e)
