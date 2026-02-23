import uuid
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from loaders.pdf_loader import load_pdf
from splitters.text_splitter import split_docs
from rag.vectorstore import (
    create_vectorstore,
    save_vectorstore,
    load_vectorstore
)
from rag.chain import build_chain

app = FastAPI()

class AskRequest(BaseModel):
    file_id: str
    question: str


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())

    docs = load_pdf(file)
    chunks = split_docs(docs)

    vectorstore = create_vectorstore(chunks)
    save_vectorstore(vectorstore, file_id)

    return {
        "message": "PDF indexed successfully",
        "file_id": file_id
    }


@app.post("/ask")
async def ask_question(req: AskRequest):
    vectorstore = load_vectorstore(req.file_id)
    chain = build_chain(vectorstore)

    result = chain.invoke(req.question)

    return {"answer": result.content}