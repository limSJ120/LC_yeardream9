import os
import retriever
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
    os.environ["GOOGLE_API_KEY"] = "AIzaSyBZmUSREZIBRfJ7TlYPHtJLHqvxkUl09vc"

    # model
while True:
    model_gemini = ChatGoogleGenerativeAI(model='gemini-pro',convert_system_message_to_humen=True,temperature=0.7)
    '''
    memory = ConversationSummaryBufferMemory(
        llm = model_gemini,
        max_token_limit = 80,
        memory_key = "chat_history",
        return_messages = True,
    )
    '''
    def load_memory(input):
        print(input)
        return memory.load_memory_variables({})["chat_history"]
    
    # 'system', 'human', 'ai'
    prompt = ChatPromptTemplate.from_messages(
        [
            ('system', "You are a helpfule assistant"),
            MessagesPlaceholder(variable_name='chat_history'),
            # ("human","{input_prompt}"),
        ]  
    )
    prompt_topic = ChatPromptTemplate.from_template(
        "tell me a history about {topic}"
    )
    chain = prompt | prompt_topic | model_gemini # RunnablePassthrough.assign(chat_history=load_memory) | 
    input_prompt = input("Question : ")
    if input_prompt.lower() == 'exit':
        break
    response = chain.invoke(
        {'chat_history' : [HumanMessage(input_prompt)],
        'topic' : "history",
        # 'question': input_prompt 
        #'chat_history' : []
        }
    )
    '''
    memory.save_context(
        {"input" : input_prompt},
        {"output" : result.content}
    )
    '''
    print(response.content)