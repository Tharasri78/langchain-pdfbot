# 📄 PDF Chatbot (Groq + LangChain RAG)

A Retrieval-Augmented Generation (RAG) based chatbot that allows users to upload a PDF document and ask questions about its content.

The system processes the document, creates semantic embeddings, stores them in a FAISS vector database, and uses Groq’s Llama model to generate accurate answers based on the document context.

---

##  Features

*  Upload and analyze PDF documents
*  Semantic search using vector embeddings
*  Fast responses using Groq LLM
*  Retrieval-Augmented Generation (RAG) pipeline
*  Local embeddings with Sentence Transformers
*  Interactive UI built with Streamlit
*  Modular architecture for easy scaling

---

## How It Works

The chatbot follows a **RAG (Retrieval-Augmented Generation)** pipeline.

1. The user uploads a PDF file.
2. The PDF is loaded and converted into text.
3. The text is split into smaller chunks.
4. Each chunk is converted into embeddings.
5. Embeddings are stored in a FAISS vector database.
6. When the user asks a question:

   * Relevant chunks are retrieved
   * Context is passed to the LLM
   * The model generates an answer based on the document.

---

##  System Architecture

```
User Question
      │
      ▼
Streamlit Interface
      │
      ▼
PDF Loader
      │
      ▼
Text Splitter
      │
      ▼
Embedding Model
      │
      ▼
FAISS Vector Database
      │
      ▼
Retriever
      │
      ▼
Groq LLM (Llama)
      │
      ▼
Generated Answer
```

---

## Project Structure

```
pdf_chatbot/
│
├── app.py
├── requirements.txt
├── .env
│
└── src/
    ├── __init__.py
    ├── pdf_loader.py
    ├── text_splitter.py
    ├── embeddings.py
    ├── vector_store.py
    └── qa_chain.py
```

### File Description

| File               | Purpose                          |
| ------------------ | -------------------------------- |
| `app.py`           | Streamlit user interface         |
| `pdf_loader.py`    | Loads PDF documents              |
| `text_splitter.py` | Splits text into chunks          |
| `embeddings.py`    | Generates vector embeddings      |
| `vector_store.py`  | Creates FAISS vector database    |
| `qa_chain.py`      | RAG pipeline and LLM interaction |

---

## 🛠️ Tech Stack

* **Python 3.11**
* **LangChain**
* **Groq API**
* **FAISS Vector Database**
* **Sentence Transformers**
* **Streamlit**
* **uv package manager**

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/pdf-chatbot.git
cd pdf-chatbot
```

---

### 2️⃣ Create Virtual Environment

Using `uv`:

```
uv venv
```

Activate environment:

Windows:

```
.venv\Scripts\activate
```

Linux / Mac:

```
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
uv pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory.

```
GROQ_API_KEY=your_groq_api_key
```

You can get a free API key from:

https://console.groq.com/

---

## ▶️ Run the Application

Start the Streamlit server:

```
uv run streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```




---

## 👨‍💻 Author

Developed as a **Generative AI learning project** demonstrating the use of Retrieval-Augmented Generation with modern LLM infrastructure.
