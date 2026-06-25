from backend.app.services.graph_visualization_service import (
    roadmap_to_reactflow_graph
)

roadmap = [
    "Python",
    "NumPy",
    "Pandas",
    "Machine Learning",
    "Deep Learning"
]

print(
    roadmap_to_reactflow_graph(
        roadmap,
        ["Python","NumPy"]
    )
)