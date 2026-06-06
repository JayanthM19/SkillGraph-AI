from fastapi import APIRouter
from backend.app.services.search_service import search_documents

router = APIRouter()

@router.get("/search")
def search(query: str):
    results = search_documents(query)

    return {
        "query": query,
        "results": results
    }