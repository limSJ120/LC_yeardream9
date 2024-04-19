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

def main():
    API_KEY = '<AIzaSyDwBT66ilp92ifgIuQyVrPwe7JZRlAf-94'
    memory2 = []
    while True:
            
        user = input("질문을 입력해주세요 : ")
        if user.lower() == 'exit':
            print(memory2)
            break
        llm = ChatGoogleGenerativeAI(model='gemini-pro', system_message_to_humen=False, temperature=0.7)
        # gemini_prompt
        #prompt_message = ChatPromptTemplate.from_messages([('system', "한국어로 대답해주고, 답변의 출처를 metadata의 source를 참조해서 알려줘"), MessagesPlaceholder(variable_name='message')])
        # Induce_topic
        # prompt_topic = ChatPromptTemplate.from_template("tell me a history about {context}")
        
        prompt = ChatPromptTemplate.from_template(
            """
            You are very,very helpful AI History professor.
            Answer the question based only on the context provided.
            system : "한국어로 대답해주고 답변의 출처를 metadata의 source를 참조해서 알려주고 \n는 없애줬으면 좋겠어."
            Context: {context}

            Question: {question}"""
        )
        
        # save_summary_buffer
        # def format_docs(docs):
        #     return "\n\n".join(doc.page_content for doc in docs)
        memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=10)
        vectorDB = TextRetriever()
        vectorlist = vectorDB.load_documents_from_csv('./joseon.csv')
        splits = vectorDB.split_documents(vectorlist)
        text_retriever = vectorDB.create_retriever(splits)
        # chain = prompt | prompt_topic | llm | text_retriever
        chain = (
        RunnablePassthrough.assign(context=(lambda x: x["question"]) | text_retriever)
        | prompt
        | llm
        | StrOutputParser()
        )
        output = chain.invoke({"question": user})
        memory.save_context({"input": user}, {"output": output})
        memory1 = memory.load_memory_variables({})
        memory2.append(memory1)
        # memory.save_context({"input": user}, {"output": output})
        print(output)
       
       
            
        # chatbot = GeminiChatbot(llm, prompt, prompt_topic, chain, memory)
        # chatbot.chat(user)
if __name__ == '__main__':
    main()