# 📄 PDF Document Q&A Bot (Groq + LangChain + Streamlit)

A simple **PDF-based Question Answering bot** built using **LangChain**, **Groq LLM**, and **Streamlit**.  
Users can upload a PDF and ask questions. The bot answers **strictly based on the document content**.

---

## 🚀 Features

- Upload PDF files
- Ask questions in natural language
- Answers are grounded only in the uploaded PDF
- Uses **Groq LLM (llama-3.1-8b-instant)**
- Simple and fast UI with Streamlit

---

## 🛠 Tech Stack

- Python 3.9+
- LangChain (LCEL / Runnable)
- Groq API
- Streamlit
- PyPDF

---

## 📁 Project Structure

Q&A/
├── app.py              # Streamlit UI
├── chain.py            # LLM + prompt logic (Groq)
├── loader.py           # PDF loader
├── splitter.py         # Text splitter
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
├── .env.example        # Environment variable template



---

## 🔧 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/USERNAME/REPO_NAME.git
cd Q&A

2️⃣ Create and activate virtual environment

Windows

python -m venv venv
venv\Scripts\activate


macOS / Linux

python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies

pip install -r requirements.txt


🔐 Environment Variables
Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key_here
⚠️ Do NOT commit .env to GitHub
Use .env.example as reference.

Get your Groq API key from:
👉 https://console.groq.com/keys

▶️ Run the Application
streamlit run app.py


Then open:

http://localhost:8501
