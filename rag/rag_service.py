import os
from dotenv import load_dotenv
import google.generativeai as genai

from rag.pdf_loader import load_pdf
from rag.chunker import chunk_text
from rag.embeddings import create_embedding
from rag.vector_store import (
    build_faiss_index,
    search_index
)

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def answer_question(pdf_path, question):

    # Load PDF
    text = load_pdf(pdf_path)

    # Chunk
    chunks = chunk_text(text)

    # Limit for testing
    chunks = chunks[:20]

    # Create embeddings
    embeddings = [
        create_embedding(chunk)
        for chunk in chunks
    ]

    # Build FAISS index
    index = build_faiss_index(
        embeddings
    )

    # Create question embedding
    query_embedding = create_embedding(
        question
    )

    # Search
    indices = search_index(
        index,
        query_embedding
    )

    # Build context
    context = ""

    for idx in indices:
        context += chunks[idx]
        context += "\n\n"

    # Gemini answer generation
    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = f"""
    Answer ONLY using the context below.

    Context:
    {context}

    Question:
    {question}
    """

    response = model.generate_content(
        prompt
    )

    return response.text