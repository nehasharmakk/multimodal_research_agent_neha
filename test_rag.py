from rag.rag_service import answer_question

result = answer_question(
    "data/reports/microsoft_annual_report_2025.pdf",
    "What are Microsoft's AI investments?"
)

print(result)










# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# from rag.pdf_loader import load_pdf
# from rag.chunker import chunk_text
# from rag.embeddings import create_embedding
# from rag.vector_store import (
#     build_faiss_index,
#     search_index
# )

# load_dotenv()

# genai.configure(
#     api_key=os.getenv("GOOGLE_API_KEY")
# )

# # Load PDF
# text = load_pdf(
#     "data/reports/microsoft_annual_report_2025.pdf"
# )

# # Chunk
# chunks = chunk_text(text)

# # Keep first 20 chunks for testing
# chunks = chunks[:20]

# # Create embeddings
# embeddings = [
#     create_embedding(chunk)
#     for chunk in chunks
# ]

# # Build FAISS
# index = build_faiss_index(
#     embeddings
# )

# # User Question
# question = "What are Microsoft's AI investments?"

# # Question embedding
# query_embedding = create_embedding(
#     question
# )

# # Retrieve relevant chunks
# indices = search_index(
#     index,
#     query_embedding
# )

# # Build context
# context = ""

# for idx in indices:
#     context += chunks[idx]
#     context += "\n\n"

# # Ask Gemini
# model = genai.GenerativeModel(
#     "gemini-2.5-flash"
# )

# prompt = f"""
# Answer ONLY using the context below.

# Context:
# {context}

# Question:
# {question}
# """

# response = model.generate_content(
#     prompt
# )

# print(response.text)