from loguru import logger # in main.py
from langchain.callbacks import FileCallbackHandler # in main.py


class Logger:
    def __init__(self):
        logfile = "output.log"

        logger.add(logfile, colorize=True, enqueue=True)
        self.handler = FileCallbackHandler(logfile)

    def print_text(self, response):
        logger.info(response)
        

logger_object = Logger() # use in main.py, gemini.py

GeminiChatbot_object = GeminiChatbot(m,m,m,m,m,m,m,m) # in main.py
response = GeminiChatbot_object.chat() # in main.py
logger_object.print_text(response) # use in main.py

logger_object.handler # use in gemini.py