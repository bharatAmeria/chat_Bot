from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dataLoader import extract_data
import os
from dotenv import load_dotenv

load_dotenv()

def create_vector_store(url):
    # Extract documents
    documents = extract_data(url)

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    # Create embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    vector_store = Chroma.from_documents(texts, embeddings)

    return vector_store

if __name__ == "__main__":
    url = "https://brainlox.com/courses/category/technical"
    vector_store = create_vector_store(url)
    print("Vector store created successfully!")
