from fastapi import APIRouter

from app.services.vector_db.vector_store_manager import (
    vector_store
)

router = APIRouter()


@router.get("/documents")
def get_documents():

    results = vector_store.get_all_documents()

    return {
        "documents": results
    }


@router.get("/database-stats")
def database_stats():

    stats = vector_store.get_stats()

    return stats


@router.delete("/reset-database")
def reset_database():

    vector_store.reset_database()

    return {
        "message": "Database reset successful"
    }