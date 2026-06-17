from backend.app.services.resume_service import (
    extract_resume_text
)

text = extract_resume_text(
    "datasets/resumes/sample_resume.pdf"
)

print(text[:1000])