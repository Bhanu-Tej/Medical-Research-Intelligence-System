from fastapi import APIRouter

from app.models.request_models import (
    QuestionRequest
)

from app.services.embeddings.embedding_generator import (
    generate_embeddings
)

from app.services.vector_db.vector_store_manager import (
    vector_store
)

from app.services.rag.rag_pipeline import (
    generate_rag_response
)

from app.services.memory.conversation_memory import (
    add_message
)

router = APIRouter()


@router.post("/ask-question")
def ask_question(
    request: QuestionRequest
):

    query_embedding = generate_embeddings(
        [request.question]
    )[0]

    retrieved_chunks = vector_store.search(
        query_embedding
    )

    response = generate_rag_response(
        request.session_id,
        request.question,
        retrieved_chunks
    )

    add_message(
        request.session_id,
        "user",
        request.question
    )

    add_message(
        request.session_id,
        "assistant",
        response
    )

    return {
        "session_id": request.session_id,
        "question": request.question,
        "answer": response,
        "sources": [
            {
                "source": chunk["source"],
                "content": chunk["content"]
            }
            for chunk in retrieved_chunks
        ]
    }