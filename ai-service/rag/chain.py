from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from rag.prompts import QA_PROMPT
from utils.env import get_env

def build_chain(vectorstore):
    llm = ChatGroq(
        api_key=get_env("GROQ_API_KEY"),
        model="llama-3.1-8b-instant",
        temperature=0
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | QA_PROMPT
        | llm
    )

    return chain