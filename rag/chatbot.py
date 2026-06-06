from dotenv import load_dotenv

from langchain_groq import ChatGroq

from rag.retriever import retriever

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

def get_rag_answer(question):

    docs = retriever.get_relevant_documents(
        question
    )

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Use only the provided context.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(
        prompt
    )

    return response.content, context