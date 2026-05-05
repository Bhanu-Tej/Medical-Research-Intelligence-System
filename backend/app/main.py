from fastapi import FastAPI

from app.api.routes.rag_routes import (
    router as rag_router
)

app = FastAPI(
    title="Medical Research Intelligence System"
)

app.include_router(
    rag_router
)

from app.api.routes.admin_routes import (
    router as admin_router
)

app.include_router(
    admin_router
)

from app.api.routes.upload_routes import (
    router as upload_router
)

app.include_router(
    upload_router
)

@app.get("/")
def home():

    return {
        "message": "Medical RAG API Running"
    }