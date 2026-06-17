from backend.app.services.role_service import (
    get_role_requirements
)

skills = get_role_requirements(
    "AI Engineer"
)

print(skills)