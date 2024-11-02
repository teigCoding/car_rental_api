# config.py

from neo4j import GraphDatabase

class Neo4jConfig:
    uri = "neo4j://localhost:7687"  # Adjust as needed for your setup
    username = "mariustage"              # Your Neo4j username
    password = "mariustage"      # Your Neo4j password

driver = GraphDatabase.driver(Neo4jConfig.uri, auth=(Neo4jConfig.username, Neo4jConfig.password))

def get_driver():
    return driver
