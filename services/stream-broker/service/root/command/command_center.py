# ex: et sw=4 ts=4 sts=4

import re
import threading

from root.base.singleton import Singleton

from root.command.notify_command import NotifyCommand
from root.command.add_command import AddCommand
from root.command.remove_command import RemoveCommand
from root.command.list_command import ListCommand

from root.util.locker import Locker

# http path
HTTP_PATH_NOTIFY        = r"/notify"
HTTP_PATH_ADD           = r"/add"
HTTP_PATH_REMOVE        = r"/remove"
HTTP_PATH_LIST          = r"/list"

@Singleton
class CommandCenter:
    
    def __init__(self):
        self._lock = threading.Lock()
    
    def execute(self, handler):
        # get path
        path = handler.request.path

        # get correct controller
        if re.match(HTTP_PATH_NOTIFY, path):
            command = NotifyCommand()
        #if re.match(HTTP_PATH_ADD, path):
        #    command = AddCommand()
        #elif re.match(HTTP_PATH_REMOVE, path):
        #    command = RemoveCommand()
        #elif re.match(HTTP_PATH_LIST, path):
        #    command = ListCommand()
        else:
            command = None

        # start command
        if command:
            command.execute(handler)
