from pydantic import BaseModel


class ResumeCareerRequest(BaseModel):
    target_role: str