import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationSummaryBufferMemory, ConversationTokenBufferMemory

from loguru import logger
from langchain.callbacks import FileCallbackHandler

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyBZmUSREZIBRfJ7TlYPHtJLHqvxkUl09vc"

logfile = "output.log"

logger.add(logfile, colorize=True, enqueue=True)
handler = FileCallbackHandler(logfile)




class GeminiChatbot:
    def __init__(self, model, prompt, prompt_topic, chain, memory):
        self.model = model
        self.prompt = prompt
        self.prompt_topic = prompt_topic
        self.chain = chain
        self.memory = memory
    # chat input, output
    def chat(self):
        while True:
            input_prompt = input("Question : ")
            if input_prompt.lower() == 'exit':
                break

            response = self.chain.invoke({'message': [HumanMessage(input_prompt)], 'topic': "history"}, {"callbacks":[handler]})
            logger.info(response)
            self.memory.save_context({"input": input_prompt}, {"output": response.content})
            print(response.content)
    # chat save_context
    def save_context(self, input_data, output_data):
        self.memory.save_context(input_data, output_data)
    # representaion
    def __repr__(self):
        return f"GeminiChatbot(model={self.model}, prompt={self.prompt}, prompt_topic={self.prompt_topic}, chain={self.chain}, memory={self.memory})"

def main():
    # model
    model_gemini = ChatGoogleGenerativeAI(model='gemini-pro', system_message_to_humen=False, temperature=0.7)
    # gemini_prompt
    prompt = ChatPromptTemplate.from_messages([('system', "You are helpful assistant."), MessagesPlaceholder(variable_name='message')])
    # Induce_topic
    prompt_topic = ChatPromptTemplate.from_template("tell me a history about {topic}")
    # chaining
    chain = prompt | prompt_topic | model_gemini 
    # save_summary_buffer
    memory = ConversationSummaryBufferMemory(llm=model_gemini, max_token_limit=10)
    # merge
    chatbot = GeminiChatbot(model_gemini, prompt, prompt_topic, chain, memory)
    chatbot.chat()

if __name__ == "__main__":
    main()