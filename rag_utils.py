# rag_utils.py

import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredHTMLLoader,
)
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

DATA_DIR = "data"
CHROMA_DB_DIR = "chroma_db"

def get_api_key():
    return os.getenv("GROQ_API_KEY", "⚠️ Missing API Key")

def load_documents():
    docs = []
    for file in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, file)
        if file.endswith(".pdf"):
            docs.extend(PyPDFLoader(path).load())
        elif file.endswith(".txt"):
            docs.extend(TextLoader(path).load())
        elif file.endswith(".docx"):
            docs.extend(UnstructuredWordDocumentLoader(path).load())
        elif file.endswith(".html"):
            docs.extend(UnstructuredHTMLLoader(path).load())
    return docs

def ingest_documents():
    documents = load_documents()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(chunks, embedding=embeddings, persist_directory=CHROMA_DB_DIR)
    vectordb.persist()
    return f"Ingested {len(chunks)} chunks into vector DB."

from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

def get_relevant_documents(query: str, k: int = 5) -> list[Document]:
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma(persist_directory=CHROMA_DB_DIR, embedding_function=embeddings)
    return vectordb.similarity_search(query, k=k)

def format_context(docs: list[Document]) -> str:
    return "\n\n---\n\n".join(doc.page_content for doc in docs)
