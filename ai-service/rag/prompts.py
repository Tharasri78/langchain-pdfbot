from langchain_core.prompts import PromptTemplate

QA_PROMPT = PromptTemplate.from_template(
"""
You are a strict document-based assistant.

Rules:
- Use ONLY the provided context
- If answer is missing, say: "Not found in document"

Context:
{context}

Question:
{question}
"""
)