import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_NAME = "gpt-4o-mini"

EMBEDDING_MODEL = "text-embedding-3-small"

VECTOR_DB_PATH = "data/processed/faiss_index"