from backend.app.services.role_service import (
    get_role_requirements
)

def calculate_role_readiness(
    user_skills,
    role
):

    required_skills = get_role_requirements(role)

    if not required_skills:
        return 0

    matched = 0

    for skill in required_skills:

        if skill in user_skills:
            matched += 1

    return round(
        (matched / len(required_skills)) * 100,
        2
    )