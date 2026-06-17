from fastapi import FastAPI
from backend.app.api.search import router as search_router
from backend.app.api.graph import (
    router as graph_router
)
from backend.app.api.career_twin import (
    router as career_router
)


from backend.app.api.hybrid import (
    router as hybrid_router
)

from backend.app.api.resume_career import (
    router as resume_router
)



app = FastAPI(
    title="SkillGraph AI",
    description="Agentic GraphRAG Career Intelligence Platform",
    version="1.0.0"
)

app.include_router(search_router)
app.include_router(graph_router)
app.include_router(hybrid_router)
app.include_router(career_router)
app.include_router(resume_router)

@app.get("/")
def home():
    return {
        "message": "SkillGraph AI Backend Running"
    }