from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re
"""
URI = "neo4j+s://65dd3b06e30036d38da32f085934c954.neo4jsandbox.com:7687"
URI = "bolt://44.197.218.79:7687"
AUTH = ("neo4j", "candidates-collector-filters")
"""
URI = "neo4j+s://65dd3b06e30036d38da32f085934c954.neo4jsandbox.com:7687"
AUTH = ("neo4j", "candidates-collector-filters")

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

def findCar(regnr):
    data = _get_connection().execute_query('MATCH (a:car) WHERE a.regnr = $regnr RETURN a;', regnr=regnr)
    return data

def updateCar(regnr):
    data = _get_connection().execute_query("MATCH (a:car) where a.name = $name RETURN a;", )
    return data

def addCar(model, make, regnr):
    data = _get_connection().execute_query("CREATE (a:car {model: $model, make: $make, regnr: $regnr}) RETURN a;", model=model, make=make, regnr=regnr)
    return data

class Car:
    def __init__(self, name, make, model, regnr):
        self.name = name
        self.make = make
        self.model = model
        self.regnr = regnr