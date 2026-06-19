from backend.app.graphrag.neo4j_connection import driver


def get_learning_path(target_skill):

    with driver.session() as session:

        result = session.run(
            """
            MATCH path =
            (start)-[:PREREQUISITE_FOR*]->(target:Skill {name:$skill})

            RETURN path
            ORDER BY length(path) DESC
            LIMIT 1
            """,
            skill=target_skill
        )

        record = result.single()

        if not record:
            return [target_skill]

        path = record["path"]

        return [
            node["name"]
            for node in path.nodes
        ]