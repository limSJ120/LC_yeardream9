import os
from langchain.callbacks import FileCallbackHandler
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from loguru import logger
# from gemini import GeminiChatbot
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyBZmUSREZIBRfJ7TlYPHtJLHqvxkUl09vc"

class logging:
    def __init__(self):
        logfile = "output.log"

        logger.add(logfile, colorize=True, enqueue=True)
        handler = FileCallbackHandler(logfile)

        llm = ChatGoogleGenerativeAI(model='gemini-pro', system_message_to_humen=False, temperature=0.7)
        prompt = PromptTemplate.from_template("1 + {number} = ")

        chain = LLMChain(llm=llm, prompt=prompt)
        answer = chain.invoke({"number":2}, {"callbacks":[handler]})
        logger.info(answer)

        # Now we can open the file output.log to see that the output has been captured.
        # %pip install --upgrade --quiet  ansi2html > /dev/null

        # from ansi2html import Ansi2HTMLConverter
        # from IPython.display import HTML, display

        # with open("output.log", "r") as f:
        #     content = f.read()

        # conv = Ansi2HTMLConverter()
        # html = conv.convert(content, full=True)

        # display(HTML(html))

log = logging()
class Logger():
    def a(self,response):
        faslkfj
    def prt_text(self,):
        logger.info()