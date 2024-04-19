import os
import csv
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

class TextRetriever:
    def __init__(self):
        if "GOOGLE_API_KEY" not in os.environ:
            os.environ["GOOGLE_API_KEY"] = "AIzaSyDwBT66ilp92ifgIuQyVrPwe7JZRlAf-94"

    # csv 파일 가져오기    
    def load_documents_from_csv(self, url):
        loader = WebBaseLoader(url)
        text = loader.load()
        return text[0]
    
    # 1000글자씩 자르고 100 글자가 겹침
    def split_documents(self, vectorlist):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        splits = text_splitter.split_documents(vectorlist)
        return splits
    
    # split 해놓은 텍스트 데이터를 embedding한 VectorDB를 생성
    def create_retriever(self, splits):
        vectordb = Chroma.from_documents(splits,
                                          embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001", temperature=0))        
        retriever = vectordb.as_retriever(k=1)
        return retriever
    
    def search(self, input_prompt, retriever):
        #response = retriever.invoke(input_prompt)
        response = retriever.get_relevant_documents(input_prompt)
        return response

# 사용 예시:
if __name__ == "__main__":
    retriever = TextRetriever()
    vectorlist = retriever.load_documents_from_csv('./joseon.csv')
    splits = retriever.split_documents(vectorlist)
    text_retriever = retriever.create_retriever(splits)
    input_prompt = input("User: ")
    response = retriever.search(input_prompt, text_retriever)
    print(response)
