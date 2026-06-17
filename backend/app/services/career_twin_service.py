from backend.app.graphrag.neo4j_connection import driver


def skill_gap_analysis(known_skills):

    query = """
    MATCH (s:Skill)-[:PREREQUISITE_FOR*]->(target)

    WHERE s.name IN $known_skills

    RETURN DISTINCT target.name AS skill
    """

    with driver.session() as session:

        result = session.run(
            query,
            known_skills=known_skills
        )

        discovered_skills = {
            record["skill"]
            for record in result
        }

    missing_skills = list(
        discovered_skills - set(known_skills)
    )

    return missing_skills