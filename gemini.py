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
from langchain.memory import ConversationSummaryBufferMemory, ConversationTokenBufferMemory
from typing import List, Any

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyBZmUSREZIBRfJ7TlYPHtJLHqvxkUl09vc"

    # model
while True:
    model_gemini = ChatGoogleGenerativeAI(model='gemini-pro',system_message_to_humen=False,temperature=0.7)
    # 'system', 'human', 'ai'
    prompt = ChatPromptTemplate.from_messages(
        [
            ('system', "You are helpful assistant."),
            MessagesPlaceholder(variable_name='message'),
        ]  
    )
    prompt_topic = ChatPromptTemplate.from_template(
        "tell me a history about {topic}"
    )
    chain = prompt | prompt_topic | model_gemini 
    input_prompt = input("Question : ")
    if input_prompt.lower() == 'exit':
        break
    memory = ConversationSummaryBufferMemory(llm=model_gemini,max_token_limit=10)
    response = chain.invoke(
        {'message' : [HumanMessage(input_prompt)],
        'topic' : "history",
        }
    )
    memory.save_context({"input":input_prompt},{"output":response.content})
    # memory.load_memory_variables({})
    print(response.content)