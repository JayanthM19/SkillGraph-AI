from backend.app.graphrag.neo4j_connection import driver


def get_next_skills(skill_name: str):

    query = """
    MATCH (s:Skill {name:$skill})
    -[:PREREQUISITE_FOR]->
    (next)

    RETURN next.name AS skill
    """

    with driver.session() as session:

        result = session.run(
            query,
            skill=skill_name
        )

        return [
            record["skill"]
            for record in result
        ]