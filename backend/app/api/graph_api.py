from fastapi import APIRouter

from backend.app.services.learning_path_service import (
    get_learning_path
)

from backend.app.services.graph_visualization_service import (
    roadmap_to_graph
)

router = APIRouter()


@router.get("/graph-roadmap")
def graph_roadmap(skill: str):

    roadmap = get_learning_path(skill)

    return roadmap_to_graph(roadmap)