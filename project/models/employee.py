from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re

# bruker local hosted neo4j fordi neo4j skulle være vanskelig
# får heller ikke loadet den employee csv filen, gjorde det på akkurat samme måte som car rental filen,
# men det skulle plutselig ikke fungere
URI = "bolt://localhost:7687"
AUTH = ("neo4j", "password")


def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()

    return driver

#jeg har comittet synd med å bruke stor E på variabel navnet, men jeg er for deep for å endre det.
def findEmployeeByEmployeename(Employee_name):
    data = _get_connection().execute_query("MATCH (a:Employee) where a.Employee_name = $Employee_name RETURN a;", Emplyee_name=Employee_name)
    if len(data[0]) > 0:
        Employee = Employee(Employee_name, data[0][0][0]['email'])
        return Employee
    else:
        return Employee(Employee_name, "Not found in DB")

class Employee:
    def __init__(self, Employee_name, email):
        self.Employee_name = Employee_name
        self.email = email

    def get_Employee_name(self):
        return self.Employee_name

    def set_Employee_name(self, value):
        self.Employee_name = value

    def get_Email(self):
        return self.email

    def set_Email(self, value):
        self.email = value