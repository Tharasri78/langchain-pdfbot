import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv(override=True)
print("DEBUG GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))


def build_chain():
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        
    )

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are a strict document assistant.
Answer ONLY using the context below.
If the answer is not in the context, say "Not found in document".

Context:
{context}

Question:
{question}
"""
    )

# LCEL: prompt → model
    chain = prompt | llm
    return chain
