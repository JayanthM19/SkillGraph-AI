from fastapi import APIRouter

from backend.app.services.hybrid_rag_service import (
    hybrid_search
)

router = APIRouter()


@router.get("/hybrid-search")
def search(skill: str):

    return hybrid_search(skill)