from backend.app.services.resume_service import (
    extract_resume_text,
    extract_skills_from_resume
)

text = extract_resume_text(
    "datasets/resumes/sample_resume.pdf"
)

skills = extract_skills_from_resume(
    text
)

print(skills)