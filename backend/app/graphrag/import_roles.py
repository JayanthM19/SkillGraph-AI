import pandas as pd

from backend.app.graphrag.neo4j_connection import driver

df = pd.read_csv("datasets/role_skills.csv")

with driver.session() as session:

    for _, row in df.iterrows():

        session.run(
            """
            MERGE (r:Role {name:$role})
            MERGE (s:Skill {name:$skill})

            MERGE (r)-[:REQUIRES]->(s)
            """,
            role=row["role"],
            skill=row["skill"]
        )

print("Roles imported successfully!")