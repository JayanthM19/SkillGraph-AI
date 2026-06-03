from fastapi import FastAPI

app = FastAPI(
    title="SkillGraph AI",
    description="Agentic GraphRAG Career Intelligence Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "SkillGraph AI Backend Running"
    }