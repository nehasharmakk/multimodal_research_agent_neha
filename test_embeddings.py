# from rag.pdf_loader import load_pdf
# from rag.chunker import chunk_text
# from rag.embeddings import create_embedding

# text = load_pdf(
#     "data/reports/microsoft_annual_report_2025.pdf"
# )

# chunks = chunk_text(text)

# embedding = create_embedding(
#     chunks[0]
# )

# print("Embedding Length:", len(embedding))

#above one was for only testing if embeddings is working now below one is using FAISS embeddings

from rag.pdf_loader import load_pdf
from rag.chunker import chunk_text
from rag.embeddings import create_embedding

from rag.vector_store import build_faiss_index

embeddings = []

text = load_pdf(
    "data/reports/microsoft_annual_report_2025.pdf"
)

chunks = chunk_text(text)

print(f"Total Chunks: {len(chunks)}")

# Build embeddings for first 10 chunks
for chunk in chunks[:10]:
    embeddings.append(
        create_embedding(chunk)
    )

index = build_faiss_index(
    embeddings
)

print("FAISS Index Size:", index.ntotal)