from fastapi import APIRouter

from backend.app.models.career_models import (
    CareerTwinRequest
)

from backend.app.services.career_twin_service import (
    skill_gap_analysis,
    generate_career_roadmap
)

router = APIRouter()


@router.post("/career-twin")

def analyze(request: CareerTwinRequest):

    missing_skills = skill_gap_analysis(
        request.known_skills
    )

    roadmap = generate_career_roadmap(
        request.known_skills,
        request.target_role,
        missing_skills
    )

    return {
        "known_skills": request.known_skills,
        "target_role": request.target_role,
        "missing_skills": missing_skills,
        "roadmap": roadmap
    }