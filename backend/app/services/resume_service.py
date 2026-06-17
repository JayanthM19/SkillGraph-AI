from pypdf import PdfReader
from backend.app.services.gemini_service import (
    generate_response
)

def extract_resume_text(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text

def extract_skills_from_resume(text):

    prompt = f"""
    Extract all technical skills from this resume.

    Return only a comma separated list.

    Resume:

    {text}
    """

    return generate_response(prompt)