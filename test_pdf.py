# from rag.pdf_loader import load_pdf

# text = load_pdf(
#     "data/reports/microsoft_annual_report_2025.pdf"
# )

# print(text[:3000])




#--------------------------------------------
#updated above one for checking chunks



# from rag.pdf_loader import load_pdf
# from rag.chunker import chunk_text

# text = load_pdf(
#     "data/reports/microsoft_annual_report_2025.pdf"
# )

# chunks = chunk_text(text)

# print(f"Total Chunks: {len(chunks)}")

# print("\nFirst Chunk:\n")
# print(chunks[0])

# print("\nSecond Chunk:\n")
# print(chunks[1])



#--------------------------------------------



from rag.pdf_loader import load_pdf
from rag.chunker import chunk_text
from rag.embeddings import create_embeddings

text = load_pdf(
    "data/reports/microsoft_annual_report_2025.pdf"
)

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

print("Number of chunks:", len(chunks))

print("Embedding shape:", embeddings.shape)