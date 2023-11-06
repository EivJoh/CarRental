from project import app
from flask import render_template, request, redirect, url_for
from project.models.employee import *

#route index
@app.route('/get_employee', methods=["POST"])
def employee1():

    if request.method == "POST":
        employee_name = request.form["name"]
        try:
            employee = findEmployeeByEmployeename(employee_name)
            data = {
                "name": employee.employee_name,
                "email": employee.email
            }
        except err:
            print (err)

    else:
        data = {
            "name": "Not specified",
            "email": "Not specified"
        }
    return render_template('employee1.html.j2', data = data)

