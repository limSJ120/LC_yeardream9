import os
from retriever import TextRetriever
from gemini import GeminiChatbot
import csv
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.callbacks.manager import(
    AsyncCallbackManagerForChainRun,
    CallbackManagerForChainRun,
)
from langchain.schema.runnable import Runnable, patch_config, RunnableParallel, RunnablePassthrough
from langchain.memory import ConversationSummaryBufferMemory
from typing import List, Any

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyDwBT66ilp92ifgIuQyVrPwe7JZRlAf-94"

vectorDB = TextRetriever()
vectorlist = vectorDB.load_documents_from_csv('./joseon.csv')
splits = vectorDB.split_documents(vectorlist)
text_retriever = vectorDB.create_retriever(splits)
gemini = GeminiChatbot()

memory2 = []
while True:
    user = input("질문을 입력해주세요 : ")
    if user.lower() == 'exit':
        print(memory2)
        break
    gemini.create_gemini_chatbot(text_retriever)
    gemini.run(gemini.chain,user)
    print(gemini.response)
    memory2.append(gemini.save_memory(user,gemini.response))
       
            
        # chatbot = GeminiChatbot(llm, prompt, prompt_topic, chain, memory)
        # chatbot.chat(user)
if __name__ == '__main__':
    main()