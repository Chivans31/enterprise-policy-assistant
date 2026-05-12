import os

from src.embed import (
    load_vector_store,
    create_vector_store
)

from src.ingest import (
    load_documents,
    split_documents
)

from src.config import VECTOR_DB_PATH


def get_retriever():

    index_file = os.path.join(
        VECTOR_DB_PATH,
        "index.faiss"
    )

    # If DB does not exist, build it
    if not os.path.exists(index_file):

        print("Vector DB not found. Building index...")

        documents = load_documents()

        chunks = split_documents(documents)

        db = create_vector_store(chunks)

    else:

        print("Loading existing vector DB...")

        db = load_vector_store()

    return db.as_retriever(
        search_kwargs={"k": 4}
    )