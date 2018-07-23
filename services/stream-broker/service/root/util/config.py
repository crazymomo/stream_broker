# ex: et sw=4 ts=4 sts=4

import os

# project directory
MODULE_ROOT         = os.path.dirname(os.path.abspath(__file__)) + '/..'

# thread count
THREAD_COUNT            = 10

# external API http port
HTTP_PORT               = 80 

# log root directory
LOG_DIR                 = '/tmp/'
# log that stores daemon messages
DAEMON_LOG_PATH = os.path.join(LOG_DIR, 'daemon.log')
