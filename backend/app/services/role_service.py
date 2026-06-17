from backend.app.graphrag.neo4j_connection import driver


def get_role_requirements(role):

    with driver.session() as session:

        result = session.run(
            """
            MATCH (r:Role {name:$role})-[:REQUIRES]->(s:Skill)
            RETURN s.name AS skill
            """,
            role=role
        )

        return [record["skill"] for record in result]