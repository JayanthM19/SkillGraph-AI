from neo4j import GraphDatabase
from backend.app.core.config import (
    NEO4J_URI,
    NEO4J_USER,
    NEO4J_PASSWORD
)

print("URI:", NEO4J_URI)

driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USER, NEO4J_PASSWORD)
)

try:
    driver.verify_connectivity()
    print("Connected Successfully!")
except Exception as e:
    print(type(e).__name__)
    print(e)