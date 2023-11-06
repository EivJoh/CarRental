from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import json

#again using the bolt localhost neo4j because the cloud one is a pain in the ass when testing
URI = "bolt://localhost:7687"
#user is neo4j, password is password
AUTH = ("neo4j", "password")

# har ikke brukt -> før i python, men etter hva jeg kan lese på nettet så er den både useful og gjør ingenting.
# denne metoden instansierer driveren som connecter til neo4j databasen. eller noe sånn
def _get_connection() -> driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

#neo4j er en graphdatabase, så formatet er en graph.
#denne metoden endrer outputtet fra node formatet til json dictionary.
def node_to_json(node):
    node_properties = dict(node.items())
    return node_properties

# får connection til neo4j, gjør queryet match employee til inputtet, og deleter det som kommer opp.
def delete_employee(reg):
    _get_connection().execute_query("MATCH(a:Employee{reg:$reg}) delete a;" reg=reg)
