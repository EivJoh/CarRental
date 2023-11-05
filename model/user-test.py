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
    def __init__(self, name, model, make, regnr):
        self.name = name
        self.model = model
        self.make = make
        self.regnr = regnr

    def get_Name(self):
        return self.name
    
    def set_Name(self, value):
        self.name = value
    
    def get_Model(self):
        return self.model
    
    def set_Model(self, value):
        self.model = value

    def get_Make(self):
        return self.make
    
    def set_Make(self, value):
        self.make = value

    def get_Regnr(self):
        return self.regnr
    
    def set_Regnr(self, value):
        self.regnr = value

#addCar("Mercedes", "3", "CF05101")
#x = findCar("CF05101")
#print(x)

"""
from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
  "bolt://44.197.218.79:7687",
  auth=basic_auth("neo4j", "candidates-collector-filters"))

cypher_query = '''
MATCH (n)
RETURN COUNT(n) AS count
LIMIT $limit
'''

with driver.session(database="neo4j") as session:
  results = session.read_transaction(
    lambda tx: tx.run(cypher_query,
                      limit="10").data())
  for record in results:
    print(record['count'])

driver.close()
"""