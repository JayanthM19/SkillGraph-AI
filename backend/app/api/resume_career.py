from fastapi import APIRouter
from backend.app.models.resume_models import (
    ResumeCareerRequest
)

router = APIRouter()

from backend.app.services.resume_service import (
    extract_resume_text,
    extract_skills_from_resume
)

from backend.app.services.career_twin_service import (
    role_based_gap_analysis,
    generate_career_roadmap
)   

@router.post("/resume-career")
def resume_career(
    request: ResumeCareerRequest
):

    text = extract_resume_text(
        "datasets/resumes/sample_resume.pdf"
    )

    skills_text = extract_skills_from_resume(
        text
    )

    skills = [
        s.strip()
        for s in skills_text.split(",")
    ]

    missing_skills = role_based_gap_analysis(
    skills,
    request.target_role
)

    roadmap = generate_career_roadmap(
        skills,
        request.target_role,
        missing_skills
)

    return {
        "extracted_skills": skills,
        "missing_skills": missing_skills,
        "roadmap": roadmap
    }