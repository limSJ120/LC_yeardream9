import os
import retriever
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationSummaryBufferMemory, ConversationTokenBufferMemory
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyDwBT66ilp92ifgIuQyVrPwe7JZRlAf-94"

class GeminiChatbot:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model='gemini-pro', system_message_to_humen=False, temperature=0.7)
        self.memory = ConversationSummaryBufferMemory(llm=self.llm, max_token_limit=10)
        self.chain = []
        self.response = []

    def save_memory(self,input_prompt,response):
        self.memory.save_context({"input": input_prompt}, {"output": response})
        memory1 = self.memory.load_memory_variables({})
        return memory1

    def create_gemini_chatbot(self,text_retriever):
        # Model
        model_gemini = ChatGoogleGenerativeAI(model='gemini-pro', system_message_to_humen=False, temperature=0.7)
        # Gemini_prompt
        prompt = ChatPromptTemplate.from_template(
                        """
                        You are very,very helpful AI History professor.
                        Answer the question based only on the context provided.
                        system : "한국어로 대답해주고 답변의 출처를 metadata의 source를 참조해서 알려주고 \n는 없애줬으면 좋겠어."
                        Context: {context}
                        Question: {question}"""
                    )
        # chaining
        self.chain = (
                    RunnablePassthrough.assign(context=(lambda x: x["question"]) | text_retriever)
                    | prompt
                    | model_gemini
                    | StrOutputParser()
                    )
        # save_chat_history
        self.memory
        return self.chain

    def run(self,chain,input_prompt):
        self.response = chain.invoke({"question": input_prompt})
        return self.response
if __name__ == "__main__":
    chatbot = create_gemini_chatbot()
    chatbot.run()
