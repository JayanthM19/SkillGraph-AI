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
from backend.app.services.resource_service import (
    get_resources
)
from backend.app.services.career_simulator_service import (
    calculate_role_readiness
)
from backend.app.services.future_simulator_service import (
    simulate_future_readiness
)
from backend.app.services.project_service import (
    recommend_projects
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

    if not skills_text:
        return {
        "error": "Unable to extract skills. Gemini quota exceeded."
    }
        
    skills = [
        s.strip()
        for s in skills_text.split(",")
    ]

    missing_skills = role_based_gap_analysis(
    skills,
    target_role
)
    readiness_score = calculate_role_readiness(
    skills,
    target_role
)
    
    future_simulation = simulate_future_readiness(
    skills,
    missing_skills,
    target_role
)
    
    recommended_projects = recommend_projects(
    missing_skills
)
    
    learning_paths = {}

    for skill in missing_skills:

        try:
            learning_paths[skill] = (
                get_learning_path(skill)
            )

        except Exception:
            learning_paths[skill] = [skill]

    
    resources = {}

    for skill in missing_skills:

        resources[skill] = get_resources(
        skill
    )
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
    "career_readiness": readiness_score,
    "future_simulation": future_simulation,
    "learning_paths": learning_paths,
    "resources": resources,
    "recommended_projects": recommended_projects,
    "unified_roadmap": unified_roadmap,
    "roadmap": roadmap
}