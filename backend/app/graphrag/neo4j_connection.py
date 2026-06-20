from neo4j import GraphDatabase
from backend.app.core.config import (
    NEO4J_URI,
    NEO4J_USER,
    NEO4J_PASSWORD
)
print("NEO4J DRIVER URI =", NEO4J_URI)
driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USER, NEO4J_PASSWORD)
)

# from neo4j import GraphDatabase

# print("URI =", NEO4J_URI)
# print("USER =", NEO4J_USER)
# print("PASSWORD EXISTS =", bool(NEO4J_PASSWORD))
# driver = GraphDatabase.driver(
#     "YOUR_URI_HERE",
#     auth=("neo4j", "YOUR_PASSWORD")
# )