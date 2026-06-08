import pandas as pd
from neo4j import GraphDatabase

from backend.app.core.config import (
    NEO4J_URI,
    NEO4J_USER,
    NEO4J_PASSWORD
)

driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USER, NEO4J_PASSWORD)
)

df = pd.read_csv("datasets/skill_relationships.csv")

with driver.session() as session:

    for _, row in df.iterrows():

        source = row["source"]
        target = row["target"]
        relationship = row["relationship"]

        query = f"""
        MERGE (a:Skill {{name: $source}})
        MERGE (b:Skill {{name: $target}})
        MERGE (a)-[:{relationship}]->(b)
        """

        session.run(
            query,
            source=source,
            target=target
        )

print("Graph imported successfully!")