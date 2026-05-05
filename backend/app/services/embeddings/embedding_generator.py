from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)


def generate_embeddings(chunks):
    """
    Generate embeddings for text chunks.
    """

    embeddings = model.encode(chunks)

    return embeddings