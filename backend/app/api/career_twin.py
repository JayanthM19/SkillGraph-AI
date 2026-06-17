from fastapi import APIRouter
from backend.app.services.career_twin_service import (
    skill_gap_analysis
)

router = APIRouter()


@router.post("/career-twin")

def analyze(skills: list[str]):

    missing = skill_gap_analysis(
        skills
    )

    return {
        "known_skills": skills,
        "missing_skills": missing
    }