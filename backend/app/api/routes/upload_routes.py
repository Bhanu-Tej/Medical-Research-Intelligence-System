import os

from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from app.services.ingestion.pdf_reader import (
    extract_text_from_pdf
)

from app.services.ingestion.text_cleaner import (
    clean_text
)

from app.services.ingestion.text_chunker import (
    chunk_text
)

from app.services.embeddings.embedding_generator import (
    generate_embeddings
)

from app.services.vector_db.vector_store_manager import (
    vector_store
)

router = APIRouter()

UPLOAD_FOLDER = "uploaded_pdfs"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


@router.post("/upload-pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        buffer.write(
            await file.read()
        )

    text = extract_text_from_pdf(
        file_path
    )

    text = clean_text(text)

    chunks = chunk_text(text)

    embeddings = generate_embeddings(
        chunks
    )

    vector_store.add_documents(
        chunks,
        embeddings,
        source=file.filename
    )

    return {
        "message": f"{file.filename} uploaded successfully",
        "chunks_added": len(chunks)
    }