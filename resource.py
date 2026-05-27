from flask import request
# creating restful API
from flask_restful import Resource

from models import Employee

from extensions import db


# --------------------------------
# GET ALL + ADD EMPLOYEE
# --------------------------------

class EmployeeListResource(Resource):

    # GET ALL EMPLOYEES
    def get(self):

        employees = Employee.query.all()

        return [

            employee.to_dict()

            for employee in employees

        ], 200


    # ADD EMPLOYEE
    def post(self):

        data = request.get_json()

        employee = Employee(

            name=data["name"],

            email=data["email"],

            department=data["department"]
        )

        db.session.add(employee)

        db.session.commit()

        return {

            "message": "Employee added successfully"

        }, 201


# --------------------------------
# SINGLE EMPLOYEE
# --------------------------------

class EmployeeResource(Resource):

    # GET SINGLE EMPLOYEE
    def get(self, id):

        employee = Employee.query.get(id)

        if not employee:

            return {
                "message": "Employee not found"
            }, 404

        return employee.to_dict(), 200


    # UPDATE EMPLOYEE
    def put(self, id):

        employee = Employee.query.get(id)

        if not employee:

            return {
                "message": "Employee not found"
            }, 404

        data = request.get_json()

        employee.name = data.get(
            "name",
            employee.name
        )

        employee.email = data.get(
            "email",
            employee.email
        )

        employee.department = data.get(
            "department",
            employee.department
        )

        db.session.commit()

        return {
            "message": "Employee updated successfully"
        }, 200


    # DELETE EMPLOYEE
    def delete(self, id):

        employee = Employee.query.get(id)

        if not employee:

            return {
                "message": "Employee not found"
            }, 404

        db.session.delete(employee)

        db.session.commit()

        return {
            "message": "Employee deleted successfully"
        }, 200