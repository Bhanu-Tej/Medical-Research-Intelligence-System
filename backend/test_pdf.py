from app.services.ingestion.pdf_reader import extract_text_from_pdf
from app.services.ingestion.text_chunker import chunk_text
from app.services.embeddings.embedding_generator import generate_embeddings
from app.services.vector_db.chroma_store import ChromaVectorStore
from app.services.rag.rag_pipeline import generate_rag_response


pdf_path = "../datasets/research_papers/diabetes.pdf"

text = extract_text_from_pdf(pdf_path)

chunks = chunk_text(text)

embeddings = generate_embeddings(chunks)

vector_store = ChromaVectorStore()

vector_store.add_documents(
    chunks,
    embeddings
)

query = "What is diabetes mellitus?"

query_embedding = generate_embeddings(
    [query]
)[0]

retrieved_chunks = vector_store.search(
    query_embedding
)

response = generate_rag_response(
    query,
    retrieved_chunks
)

print("\nAI RESPONSE:\n")

print(response)