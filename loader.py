from langchain_community.document_loaders import PyPDFLoader

import tempfile
import os

def load_pdf(uploaded_file):
    # Save uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    loader = PyPDFLoader(tmp_path)
    docs = loader.load()

    os.remove(tmp_path)
    return docs
