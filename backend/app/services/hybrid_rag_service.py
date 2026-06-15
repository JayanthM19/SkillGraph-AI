from backend.app.services.graph_service import (
    get_next_skills
)

from backend.app.rag.embedding_service import (
    search_documents
)

from backend.app.services.gemini_service import (
    generate_response
)


def hybrid_search(skill):

    graph_results = get_next_skills(skill)

    vector_results = search_documents(skill)

    prompt = f"""
    User knows: {skill}

    Recommended skills:
    {graph_results}

    Learning context:
    {vector_results}

    Explain:
    1. What should the user learn next?
    2. Why?
    3. Suggested roadmap.
    """

    answer = generate_response(prompt)

    return {
        "skill": skill,
        "recommendations": graph_results,
        "answer": answer
    }