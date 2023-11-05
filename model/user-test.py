from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re

#URI = "neo4j+s://65dd3b06e30036d38da32f085934c954.neo4jsandbox.com:7687"
URI = "bolt://44.197.218.79:7687"
AUTH = ("neo4j", "candidates-collector-filters")

def _get_connection() -> Driver:
    # driver = GraphDatabase.driver(URI, auth=AUTH)
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

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