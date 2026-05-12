import json

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

from src.chain import build_rag_chain
from src.retrieve import get_retriever
#from src.reranker import rerank

app = FastAPI()

retriever = get_retriever()
rag_chain = build_rag_chain()


class QueryRequest(BaseModel):
    question: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask-stream")
def ask_stream(request: QueryRequest):

    def generate():

        refined_docs = retriever.invoke(
             request.question)
        

        # Sources
        sources = [
            {
                "source": d.metadata.get("source"),
                "page": d.metadata.get("page")
            }
            for d in refined_docs
        ]

        # Send metadata first
        yield (
            json.dumps({"sources": sources})
            + "\n--END_METADATA--\n"
        )

        # Build context
        context = "\n\n".join(
            d.page_content
            for d in refined_docs
        )

        # Stream answer
        for chunk in rag_chain.stream(
            {
                "context": context,
                "question": request.question
            }
        ):
            yield chunk

    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )
import os

if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))

    uvicorn.run(
        "src.api:app",
        host="0.0.0.0",
        port=port
    )