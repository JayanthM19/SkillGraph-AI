from backend.app.services.career_simulator_service import (
    calculate_role_readiness
)

skills = [
    "Python",
    "Machine Learning",
    "Deep Learning"
]

print(
    calculate_role_readiness(
        skills,
        "AI Engineer"
    )
)