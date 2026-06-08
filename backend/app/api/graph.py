from fastapi import APIRouter

from backend.app.services.graph_service import (
    get_next_skills
)

router = APIRouter()


@router.get("/recommend")

def recommend(skill: str):

    recommendations = get_next_skills(skill)

    return {
        "known_skill": skill,
        "recommended_skills": recommendations
    }