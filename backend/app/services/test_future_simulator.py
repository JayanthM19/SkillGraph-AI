from backend.app.services.future_simulator_service import (
    simulate_future_readiness
)

skills = [
    "Python",
    "Machine Learning"
]

missing = [
    "Transformers",
    "Embeddings",
    "RAG"
]

print(
    simulate_future_readiness(
        skills,
        missing,
        "AI Engineer"
    )
)