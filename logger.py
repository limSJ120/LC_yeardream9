from langchain.callbacks import FileCallbackHandler
from loguru import logger

class Logger:
    def __init__(self, filename):
        self.logfile = filename

        logger.add(self.logfile, colorize=True, enqueue=True)
        self.handler = FileCallbackHandler(self.logfile)

    def print_text(self, response):
        logger.info(response)