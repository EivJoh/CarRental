from neo4j import GraphDatabase, Driver
import json

URI = "neo4j+ssc://3a473ef7.databases.neo4j.io"
AUTH = ("neo4j", "_1-CfKipSOy-1qghMbqCeOYBaJN_pUU0TnfBOwFEm4s")

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

def node_to_json(node):
    node_properties = dict(node.items())
    return node_properties

def findAllCars():
    with _get_connection().session() as session:
        cars = session.run("MATCH (n:Cars) RETURN n;")
        nodes_json = [node_to_json(record["n"]) for record in cars]
        print(nodes_json)
        return nodes_json

def findAllEmployees():
    with _get_connection().session() as session:
        employees = session.run("MATCH (n:Employees) RETURN n;")
        nodes_json = [node_to_json(record["n"]) for record in employees]
        print(nodes_json)
        return nodes_json

def findAllCustomers():
    with _get_connection().session() as session:
        customers = session.run("MATCH (n:Customers) RETURN n;")
        nodes_json = [node_to_json(record["n"]) for record in customers]
        print(nodes_json)
        return nodes_json


def update_car(Brand, Model, Reg, Year, Status, Color):
    with _get_connection().session() as session:
        cars = session.run("MATCH (n:Cars{Reg:$Reg}) SET n.Brand=$Brand, n.Model=$Model, n.Year=$Year, n.Status=$Status, n.Color=$Color RETURN n;", Reg=Reg, Brand=Brand, Model=Model, Year=Year, Status=Status, Color=Color)
        print(cars)
        nodes_json = [node_to_json(record["n"]) for record in cars]
        print(nodes_json)
        return nodes_json

def update_employee(EmployeeID, Email, Branch, Employee_name):
    with _get_connection().session() as session:
        employees = session.run("MATCH (n:Employees{EmployeeID:$EmployeeID}) SET n.Email=$Email, n.Branch=$Branch, n.Employee_name=$Employee_name RETURN n;", EmployeeID=EmployeeID, Email=Email, Branch=Branch, Employee_name=Employee_name)
        print(employees)
        nodes_json = [node_to_json(record["n"]) for record in employees]
        print(nodes_json)
        return nodes_json

def update_customer(CustomerID, Email, Adress, Customer_name, Phone_Number):
    with _get_connection().session() as session:
        customer = session.run("MATCH (n:Customers{CustomerID:$CustomerID}) SET n.Email=$Email, n.Adress=$Adress, n.Customer_name=$Customer_name, n.Phone_Number=$Phone_Number RETURN n;", CustomerID=CustomerID, Email=Email, Adress=Adress, Customer_name=Customer_name, Phone_Number=Phone_Number)
        print(customer)
        nodes_json = [node_to_json(record["n"]) for record in customer]
        print(nodes_json)
        return nodes_json

#Create car, employee, customer
# får typeError: string indicis must be integers, not "str", men funksjonen funker?
def create_car(Brand, Model, Reg, Year, Status, Color):
    cars = _get_connection().execute_query("MERGE (n:Cars{Brand: $Brand, Model: $Model, Reg: $Reg, Year: $Year, Status:$Status, Color:$Color}) RETURN n;", Reg=Reg, Brand=Brand, Model=Model, Year=Year, Status=Status, Color=Color)
    nodes_json = [node_to_json(record["n"]) for record in cars]
    print(nodes_json)
    return nodes_json

def create_employee(EmployeeID, Email, Branch, Employee_name):
    employees = _get_connection().execute_query("MERGE (n:Employees{EmployeeID: $EmployeeID, Email: $Email, Branch: $Branch, Employee_name: $Employee_name}) RETURN n;", EmployeeID=EmployeeID, Email=Email, Branch=Branch, Employee_name=Employee_name)
    nodes_json = [node_to_json(record["n"]) for record in employees]
    print(nodes_json)
    return nodes_json

def create_customer(CustomerID, Email, Adress, Customer_name, Phone_Number):
    customers = _get_connection().execute_query("MERGE (n:Customers{CustomerID: $CustomerID, Email: $Email, Adress: $Adress, Customer_name: $Customer_name, Phone_Number: $Phone_Number}) RETURN n;", CustomerID=CustomerID, Email=Email, Adress=Adress, Customer_name=Customer_name, Phone_Number=Phone_Number)
    nodes_json = [node_to_json(record["n"]) for record in customers]
    print(nodes_json)
    return nodes_json

# delete car, customer, employee

def delete_car(Reg):
    _get_connection().execute_query("MATCH(n:Cars{Reg:$Reg}) DELETE n;", Reg=Reg)

def delete_employee(EmployeeID):
    _get_connection().execute_query("MATCH(n:Employees{EmployeeID:$EmployeeID}) DELETE n;", EmployeeID=EmployeeID)

def delete_customer(CustomerID):
    _get_connection().execute_query("MATCH(n:Customers{CustomerID:$CustomerID}) DELETE n;", CustomerID=CustomerID)

#order car
def findCarByReg(Reg):
    with _get_connection().session() as session:
        cars = session.run("MATCH(n:Cars) where n.Reg=$Reg RETURN n;", Reg=Reg)
        print(cars)
        nodes_json = [node_to_json(record["n"])for record in cars]
        print(nodes_json)
        return nodes_json

##### IKKE FERDIG ENDA
def order_car(CustomerID, Reg):
    with _get_connection().session() as session:
        #queries if the customer matching the CustomerID has the relationship RENTING, and returns the answer as count.
        customer = session.run("MATCH(n:Customers {CustomerID:$CustomerID})-[:RENTING]->(car:Cars) RETURN COUNT(car) as count;", CustomerID=CustomerID)
        print(customer)
        #if the count is higher than 0, meaning the customer is already renting a car, return already renting car
        if customer["count"] > 0:
            return jsonify({"already renting a car"})
        else:
            #else create the relationship customer matching CustomerID RENTING car matching Reg.
            with session.run("""
            MATCH (n:Customers {CustomerID:$CustomerID})
            MATCH (a:Cars {Reg:$Reg})
            Create (n)-[:RENTING]->(a)
            """, Reg=Reg, CustomerID=CustomerID)
        #unsure how to return this
        return