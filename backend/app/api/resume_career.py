from fastapi import APIRouter
from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form
)
from backend.app.models.resume_models import (
    ResumeCareerRequest
)
from backend.app.services.learning_path_service import (
    get_learning_path
)
from backend.app.services.roadmap_service import (
    build_unified_roadmap
)
from backend.app.services.file_service import (
    save_uploaded_file
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
    file: UploadFile = File(...),
    target_role: str = Form(...)
):
    file_path = save_uploaded_file(
    file
)
    text = extract_resume_text(
    file_path
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
    target_role
)
    learning_paths = {}

    for skill in missing_skills:

        try:
            learning_paths[skill] = (
                get_learning_path(skill)
            )

        except Exception:
            learning_paths[skill] = [skill]

    unified_roadmap = build_unified_roadmap(
    learning_paths
)
    
    roadmap = generate_career_roadmap(
        skills,
        target_role,
        missing_skills
)

    return {
    "extracted_skills": skills,
    "missing_skills": missing_skills,
    "learning_paths": learning_paths,
    "unified_roadmap": unified_roadmap,
    "roadmap": roadmap
}