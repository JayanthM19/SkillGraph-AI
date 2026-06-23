def roadmap_to_graph(
    roadmap,
    user_skills=None
):

    if user_skills is None:
        user_skills = []

    nodes = []
    edges = []

    for skill in roadmap:

        status = (
            "completed"
            if skill in user_skills
            else "missing"
        )

        nodes.append({
            "id": skill,
            "label": skill,
            "status": status
        })

    for i in range(len(roadmap) - 1):

        edges.append({
            "source": roadmap[i],
            "target": roadmap[i + 1]
        })

    return {
        "nodes": nodes,
        "edges": edges
    }