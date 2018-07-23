# ex: et sw=4 ts=4 sts=4

import json

from root.command.command import Command

from root.stream.stream_center import StreamCenter

from root.util.system_util import system
from root.util.config import MODULE_ROOT

class AddCommand(Command):
    
    def __init__(self):
        super().__init__()
    
    def execute(self, handler):
        try:
            # add to stream center
            StreamCenter.getInstance().add(stream_name)
        except Exception as e:
            self._logger.debug(e)
            # return result
            handler.set_status(400)
            handler.write('')

