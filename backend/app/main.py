from fastapi import FastAPI
from backend.app.api.search import router as search_router
from backend.app.api.graph import (
    router as graph_router
)


app = FastAPI(
    title="SkillGraph AI",
    description="Agentic GraphRAG Career Intelligence Platform",
    version="1.0.0"
)

app.include_router(search_router)
app.include_router(graph_router)
@app.get("/")
def home():
    return {
        "message": "SkillGraph AI Backend Running"
    }