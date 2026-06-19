from backend.app.services.learning_path_service import (
    get_learning_path
)

path = get_learning_path(
    "Kubernetes"
)

print(path)