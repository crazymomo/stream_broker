# ex: et sw=4 ts=4 sts=4

import sys

from root.web.server import Server

from root.util.log_util import Logger, setup_logger
from root.util.config import HTTP_PORT
 
def main():
    # setup logger
    setup_logger();
    
    # start server
    server = Server()
    server.start(HTTP_PORT)

if __name__ == "__main__":
    main()
