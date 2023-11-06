from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re

URI = "neo4j+s://65dd3b06e30036d38da32f085934c954.neo4jsandbox.com:7687"
AUTH = ("neo4j", "candidates-collector-filters")

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

def updateCustomer():
    with _get_connection().session() as session:
        ()
        
def deleteCustomer():
    with _get_connection().session() as session:
        ()