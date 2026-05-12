import os

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from src.config import VECTOR_DB_PATH


def create_vector_store(chunks):

    embeddings = OpenAIEmbeddings()

    db = FAISS.from_documents(
        chunks,
        embeddings
    )

    os.makedirs(
        VECTOR_DB_PATH,
        exist_ok=True
    )

    db.save_local(VECTOR_DB_PATH)

    return db


def load_vector_store():

    embeddings = OpenAIEmbeddings()

    return FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )