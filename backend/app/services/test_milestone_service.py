from backend.app.services.milestone_service import get_milestones

roadmap = [
    "Python",
    "NumPy",
    "Pandas"
]

print(get_milestones(roadmap))