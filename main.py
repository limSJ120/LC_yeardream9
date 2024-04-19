import os
from retrie_class import TextRetriever
from gemini import GeminiChatbot
import csv
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

def main():
    API_KEY = '<Your API KEY>'
    user = input("질문을 입력해주세요 : ")
    model_gemini = ChatGoogleGenerativeAI(model='gemini-pro', system_message_to_humen=False, temperature=0.7)
    # gemini_prompt
    prompt = ChatPromptTemplate.from_messages([('system', "한국어로 대답해주고, 답변의 출처를 metadata의 source를 참조해서 알려줘"), MessagesPlaceholder(variable_name='message')])
    # Induce_topic
    prompt_topic = ChatPromptTemplate.from_template("tell me a history about {topic}")
    # chaining
    chain = prompt | prompt_topic | model_gemini 
    # save_summary_buffer

    memory = ConversationSummaryBufferMemory(llm=model_gemini, max_token_limit=10)
    vectorDB = TextRetriever()

    vectorlist = vectorDB.load_documents_from_csv('./joseon.csv')
    splits = vectorDB.split_documents(vectorlist)
    text_retriever = vectorDB.create_retriever(splits)
    response = vectorDB.search(user,text_retriever)
    chatbot = GeminiChatbot(model_gemini, prompt, prompt_topic, chain, memory,response)
    chatbot.chat(user)
if __name__ == '__main__':
    main()