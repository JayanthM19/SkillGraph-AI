from backend.app.services.multi_role_service import (
    get_role_rankings
)

skills = [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow"
]

print(
    get_role_rankings(
        skills
    )
)