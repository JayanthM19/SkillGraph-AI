from backend.app.services.graph_visualization_service import (
    roadmap_to_graph
)

roadmap = [
    "Python",
    "NumPy",
    "Pandas",
    "Machine Learning",
    "RAG"
]

user_skills = [
    "Python",
    "NumPy"
]

print(
    roadmap_to_graph(
        roadmap,
        user_skills
    )
)