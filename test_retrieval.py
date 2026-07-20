from rag.pdf_loader import load_pdf
from rag.chunker import chunk_text
from rag.embeddings import create_embedding
from rag.vector_store import (
    build_faiss_index,
    search_index
)

text = load_pdf(
    "data/reports/microsoft_annual_report_2025.pdf"
)

chunks = chunk_text(text)

# Use first 20 chunks for now
chunks = chunks[:20]

embeddings = [
    create_embedding(chunk)
    for chunk in chunks
]

index = build_faiss_index(
    embeddings
)

question = "What are Microsoft's AI investments?"

query_embedding = create_embedding(
    question
)

results = search_index(
    index,
    query_embedding
)

print("Top matching chunks:")

for idx in results:
    print("\n=================\n")
    print(chunks[idx][:500])