"""
日志信息模块
"""
import os
from loguru import logger
from flaskapp.tools import SingleInstance
from flaskapp.settings import LOG_PATH, LOG_FILE


class LoggerHelp(object):
    def __init__(self):
        self.logger = logger
        if not os.path.exists(LOG_PATH):
            os.makedirs(LOG_PATH)
        self.logger.add("%s" % LOG_FILE, rotation="1024MB", retention=1)

    def write(self, message, level='debug'):
        if level == 'debug':
            self.logger.debug(message)
        elif level == 'info':
            self.logger.info(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'critical':
            self.logger.critical(message)
        elif level == 'exception':
            self.logger.exception(message)
        elif level == 'error':
            self.logger.error(message)



if __name__ == "__main__":
    log = LoggerHelp()
    log.write("hello", level='debug')


        