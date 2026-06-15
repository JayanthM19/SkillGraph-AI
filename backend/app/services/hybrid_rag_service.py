from backend.app.services.graph_service import (
    get_next_skills
)

from backend.app.rag.embedding_service import (
    search_documents
)


def hybrid_search(skill):

    graph_results = get_next_skills(skill)

    vector_results = search_documents(skill)

    return {
        "skill": skill,
        "graph_recommendations": graph_results,
        "vector_context": vector_results
    }