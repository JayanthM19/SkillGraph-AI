from fastapi import FastAPI
from backend.app.api.search import router as search_router

app = FastAPI(
    title="SkillGraph AI",
    description="Agentic GraphRAG Career Intelligence Platform",
    version="1.0.0"
)

app.include_router(search_router)

@app.get("/")
def home():
    return {
        "message": "SkillGraph AI Backend Running"
    }