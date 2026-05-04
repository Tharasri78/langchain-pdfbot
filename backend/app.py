import streamlit as st
import tempfile
import os
from src.pdf_loader import load_pdf
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.qa_chain import create_qa_chain

# Page Configuration
st.set_page_config(
    page_title="PDF Chatbot | Groq + LangChain",
    page_icon="📄",
    layout="wide"
)

# Custom CSS for Premium Look
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1e1e2f 0%, #121212 100%);
        color: #ffffff;
    }
    .stTextInput > div > div > input {
        background-color: #2d2d44;
        color: #ffffff;
        border-radius: 10px;
        border: 1px solid #3d3d5c;
    }
    .stButton > button {
        background-color: #6c5ce7;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #a29bfe;
        transform: translateY(-2px);
    }
    .chat-bubble {
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
        max-width: 80%;
    }
    .user-bubble {
        background-color: #3d3d5c;
        align-self: flex-end;
    }
    .bot-bubble {
        background-color: #2d2d44;
        border: 1px solid #6c5ce7;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar for Upload and Info
with st.sidebar:
    st.title("📄 PDF Settings")
    st.markdown("---")
    uploaded_file = st.file_uploader("Upload your document", type="pdf")
    
    if uploaded_file:
        st.success("File uploaded successfully!")
        if st.button("Process PDF"):
            with st.spinner("Processing document... This may take a moment."):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                    temp_file.write(uploaded_file.read())
                    temp_file_path = temp_file.name
                
                try:
                    docs = load_pdf(temp_file_path)
                    chunks = split_documents(docs)
                    vector_store = create_vector_store(chunks)
                    qa_chain = create_qa_chain(vector_store)
                    
                    st.session_state.qa_chain = qa_chain
                    st.session_state.chat_history = []
                    st.success("Indexing complete! Ask away.")
                except Exception as e:
                    st.error(f"Error processing PDF: {e}")
                finally:
                    if os.path.exists(temp_file_path):
                        os.remove(temp_file_path)
    
    st.markdown("---")
    st.info("Built with Groq (Llama 3.1) & LangChain")

# Main Chat Interface
st.title("🤖 Intelligent PDF Assistant")
st.markdown("Ask questions about your uploaded PDF and get instant, context-aware answers.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if "qa_chain" in st.session_state:
    if prompt := st.chat_input("How can I help you with this document?"):
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.chat_history.append({"role": "user", "content": prompt})

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = st.session_state.qa_chain.invoke(prompt)
                    st.markdown(response)
                    st.session_state.chat_history.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"Error generating response: {e}")
else:
    st.warning("Please upload and process a PDF document in the sidebar to start chatting.")