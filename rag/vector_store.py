import faiss
import numpy as np
def build_faiss_index(embeddings):

    embeddings = np.array(
        embeddings,
        dtype="float32"
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index
def search_index(index, query_embedding, top_k=3):

    import numpy as np

    query_vector = np.array(
        [query_embedding],
        dtype="float32"
    )

    distances, indices = index.search(
        query_vector,
        top_k
    )

    return indices[0]


