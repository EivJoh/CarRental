import json
from project import app
from flask import render_template, request, redirect, url_for
from project.models.my_dao import *

# read cars, employees, customers.
@app.route("/get_cars", methods=["GET"])
def query_records():
    return findAllCars()

@app.route("/get_employees", methods=["GET"])
def query_employees():
    return findAllEmployees()

@app.route("/get_customers", methods=["GET"])
def query_customers():
    return findAllCustomers()


#update car, employees, customers, see notes.
@app.route("/update_car", methods=["PUT"])
def update_car_info():
    record = json.loads(request.data)
    print(record)
    return update_car(record["Brand"],record["Model"],record["Reg"],record["Year"],record["Status"],record["Color"])


@app.route("/update_employee", methods=["PUT"])
def update_employee_info():
    record = json.loads(request.data)
    print(record)
    return update_employee(record["EmployeeID"],record["Email"],record["Branch"],record["Employee_name"])

@app.route("/update_customer", methods=["PUT"])
def update_customer_info():
    record = json.loads(request.data)
    print(record)
    return update_customer(record["CustomerID"],record["Email"],record["Adress"],record["Customer_name"], record["Phone_Number"])

# create car, employee, customer

@app.route('/create_car', methods=["POST"])
def create_car_info():
    record = json.loads(request.data)
    print(record)
    return create_car(record["Brand"],record["Model"],record["Reg"],record["Year"],record["Status"],record["Color"])

@app.route('/create_employee', methods=["POST"])
def create_employee_info():
    record = json.loads(request.data)
    print(record)
    return create_employee(record["EmployeeID"],record["Email"],record["Branch"],record["Employee_name"])

@app.route('/create_customer', methods=["POST"])
def create_customer_info():
    record = json.loads(request.data)
    print(record)
    return create_customer(record["CustomerID"],record["Email"],record["Adress"],record["Customer_name"], record["Phone_Number"])

#delete funksjoner
@app.route("/delete_car", methods=["DELETE"])
def delete_car_info():
    record = json.loads(request.data)
    print(record)
    delete_car(record["Reg"])
    return findAllCars()

@app.route("/delete_employee", methods=["DELETE"])
def delete_employee_info():
    record = json.loads(request.data)
    print(record)
    delete_employee(record["EmployeeID"])
    return findAllEmployees()

@app.route("/delete_customer", methods=["DELETE"])
def delete_customer_info():
    record = json.loads(request.data)
    print(record)
    delete_customer(record["CustomerID"])
    return findAllCustomers()

@app.route("/order_car", methods=["GET", "POST"])
def order_car_info():
    record = json.loads(request.data)
    print(record)
    return order_car(record["Reg"],record["CustomerID"])