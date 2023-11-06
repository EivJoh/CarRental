from project import app
from flask import render_template, request, redirect, url_for
#importing everything from the models file that this controller controls.
from project.models.delete_employee_model import *

#creating new route, delete_employee
@app.route("/delete_employee", methods=["DELETE"])
def delete_employee():
    record = json.loads(request.data)
    print(record)
    delete_car(record["reg"])
    #method findAllEmployees() does not exist yet
    #meant to return all employees to display the remaining employees after one is deleted.
    return findAllEmployees()

# employee2 html er bare det samme som employee1 html atm, ettersom at delete employee ikke returner noe enda.