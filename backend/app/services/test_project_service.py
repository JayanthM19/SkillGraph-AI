from backend.app.services.project_service import (
    recommend_projects
)

missing = [
    "RAG",
    "LangChain",
    "LangGraph"
]

print(
    recommend_projects(
        missing
    )
)