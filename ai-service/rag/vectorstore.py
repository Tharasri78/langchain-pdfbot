import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

BASE_DIR = "vectorstores"

def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

def create_vectorstore(chunks):
    embeddings = get_embeddings()
    return FAISS.from_documents(chunks, embeddings)

def save_vectorstore(vectorstore, file_id: str):
    path = os.path.join(BASE_DIR, file_id)
    os.makedirs(path, exist_ok=True)
    vectorstore.save_local(path)

def load_vectorstore(file_id: str):
    embeddings = get_embeddings()
    path = os.path.join(BASE_DIR, file_id)
    if not os.path.exists(path):
        raise FileNotFoundError("Vectorstore not found")
    return FAISS.load_local(
        path, embeddings, allow_dangerous_deserialization=True
    )