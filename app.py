import streamlit as st
import tempfile

from src.pdf_loader import load_pdf
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.qa_chain import create_qa_chain


st.title("PDF Chatbot")


uploaded_file = st.file_uploader("Upload a PDF", type="pdf")


if uploaded_file and "qa_chain" not in st.session_state:

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        file_path = temp_file.name

    st.write("Processing PDF...")

    docs = load_pdf(file_path)

    chunks = split_documents(docs)

    vector_store = create_vector_store(chunks)

    qa_chain = create_qa_chain(vector_store)

    st.session_state.qa_chain = qa_chain


if "qa_chain" in st.session_state:

    question = st.text_input("Ask a question about the PDF")

    if question:

        response = st.session_state.qa_chain.invoke(question)

        st.write(response)