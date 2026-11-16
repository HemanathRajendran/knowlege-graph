from neo4j import GraphDatabase
import os

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(
        os.getenv("NEO4J_USERNAME"),
        os.getenv("NEO4J_PASSWORD")
    )
)

def insert_scheme(data):

    query = """
    MERGE (s:Scheme {
      name:$name
    })

    SET s.url=$url
    """

    with driver.session() as session:

        session.run(
            query,
            name=data["name"],
            url=data["url"]
        )