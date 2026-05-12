from langchain_openai import ChatOpenAI
#from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

#from src.retrieve import get_retriever
from src.config import MODEL_NAME
#from src.reranker import rerank


def build_rag_chain():

    llm = ChatOpenAI(
        model=MODEL_NAME,
        temperature=0,
        streaming=True
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are an enterprise policy assistant.

Answer ONLY using the provided context.

If the answer is not in the context, say:
'I could not find that information in the provided documents.'

Context:
{context}

Question:
{question}

Answer:
"""
    )

    chain = (
        prompt
        | llm
        | StrOutputParser()
    )

    return chain

