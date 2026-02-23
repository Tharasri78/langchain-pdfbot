import tempfile
import os
from fastapi import UploadFile
from langchain_community.document_loaders import PyPDFLoader

def load_pdf(upload_file: UploadFile):
    if upload_file.content_type != "application/pdf":
        raise ValueError("Only PDF files are allowed")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(upload_file.file.read())
        path = tmp.name

    try:
        loader = PyPDFLoader(path)
        docs = loader.load()
        if not docs:
            raise ValueError("PDF contains no readable text")
        return docs
    finally:
        os.remove(path)