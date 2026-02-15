import streamlit as st
from loader import load_pdf
from splitter import split_docs
from chain import build_chain

st.set_page_config(page_title="PDF Q&A Bot", layout="centered")
st.title("📄 PDF Document Q&A")

uploaded_file = st.file_uploader(
    "Upload a PDF file",
    type=["pdf"]
)

if uploaded_file:
    with st.spinner("Processing PDF..."):
        docs = load_pdf(uploaded_file)
        chunks = split_docs(docs)
        context = "\n\n".join(chunk.page_content for chunk in chunks)
        chain = build_chain()

    st.success("PDF loaded successfully!")

    # ✅ QUESTION INPUT (YOU WERE MISSING THIS)
    question = st.text_area("Ask a question from the PDF")

    if st.button("Get Answer"):
        if question.strip() == "":
            st.warning("Ask a valid question.")
        else:
            with st.spinner("Thinking..."):
                response = chain.invoke({
                    "context": context,
                    "question": question
                })
                answer = response.content

            st.subheader("Answer")
            st.write(answer)
else:
    st.info("Please upload a PDF to start.")
