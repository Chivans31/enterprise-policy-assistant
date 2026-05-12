import sys
import os

# FIX IMPORT PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ingest import load_documents, split_documents
from src.embed import create_vector_store


def main():
    docs = load_documents()
    chunks = split_documents(docs)
    create_vector_store(chunks)
    print("Vector DB created!")


if __name__ == "__main__":
    main()