from src.embed import load_vector_store
#from rank_bm25 import BM25Okapi
#import pickle


def get_retriever():
    db = load_vector_store()
    return db.as_retriever(search_kwargs={"k": 8})