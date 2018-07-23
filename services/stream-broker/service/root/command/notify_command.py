# ex: et sw=4 ts=4 sts=4

import json

from root.command.command import Command

from root.stream.stream_center import StreamCenter

from root.util.system_util import system
from root.util.config import MODULE_ROOT

class NotifyCommand(Command):
    
    def __init__(self):
        super().__init__()
    
    def execute(self, handler):
        try:
            # get remote ip
            remote_ip = handler.request.headers.get("X-Forwarded-For")
            remote_ip = remote_ip if remote_ip else handler.request.remote_ip

            # show arguments
            #self._logger.debug(handler.request.arguments)

            # get notify type and stream name
            notify_type = handler.get_argument('call');
            stream_name = handler.get_argument('name');

            # add to stream center
            if notify_type == 'publish':
                StreamCenter.getInstance().add(remote_ip, stream_name)
            # remove from stream server
            elif notify_type == 'publish_done':
                StreamCenter.getInstance().remove(remote_ip, stream_name)
        except Exception as e:
            # show error
            self._logger.debug(e)
            # return result
            handler.set_status(400)
            handler.write('')

