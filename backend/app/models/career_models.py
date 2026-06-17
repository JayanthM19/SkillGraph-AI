from pydantic import BaseModel


class CareerTwinRequest(BaseModel):
    known_skills: list[str]
    target_role: str