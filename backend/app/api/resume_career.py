from fastapi import APIRouter

router = APIRouter()

from backend.app.services.resume_service import (
    extract_resume_text,
    extract_skills_from_resume
)

from backend.app.services.career_twin_service import (
    skill_gap_analysis,
    generate_career_roadmap
)   

@router.get("/resume-career")
def resume_career():

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

    missing_skills = skill_gap_analysis(
        skills
    )

    roadmap = generate_career_roadmap(
        skills,
        "AI Engineer",
        missing_skills
    )

    return {
        "extracted_skills": skills,
        "missing_skills": missing_skills,
        "roadmap": roadmap
    }