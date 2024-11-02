from neo4j import GraphDatabase

class Neo4jConfig:
    uri = "neo4j://localhost:7687"  
    username = "mariustage"            
    password = "mariustage"      

driver = GraphDatabase.driver(Neo4jConfig.uri, auth=(Neo4jConfig.username, Neo4jConfig.password))

def get_driver():
    return driver
