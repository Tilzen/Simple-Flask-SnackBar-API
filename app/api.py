from app import app, session
from flask import request, jsonify
from flask_restful import Api, Resource
from flask_restful.reqparse import RequestParser
from markdown import markdown
from app.models import (Employees, SnackMenu,
                        EmployeesSchema, SnackMenuSchema)

api = Api(app)

# definition of snacks schemas
snack_schema = SnackMenuSchema(strict=True)
snacks_schema = SnackMenuSchema(many=True, strict=True)

# definition of employees schemas
employee_schema = EmployeesSchema(strict=True)
employees_schema = EmployeesSchema(many=True, strict=True)


@app.route('/docs')
@app.route('/documentation')
def documentation():
    """
    Displays the API documentation.
    """
    readme_file_path = app.root_path + '/../README.md'

    with open(readme_file_path, 'r') as readme_file:
        readme_content = readme_file.read()
        return markdown(readme_content)


class EmployeeResource(Resource):
    """
    Implementation of specific employee manipulation methods defined by employee_id.
    """

    def get(self, employee_id):
        """
        Get a specific employee in the database.
        """
        employee = Employees.query.get(employee_id)
        return employee_schema.jsonify(employee)


    def put(self, employee_id):
        """
        Updates the employee data.
        """
        employee = Employees.query.get(employee_id)

        employee.employee_name = request.json['employee_name']
        employee.employee_role = request.json['employee_role']
        employee.employee_salary = request.json['employee_salary']
        result = employee_schema.dump(employee)

        session.commit()
        return jsonify(result)


    def delete(self, employee_id):
        """
        Delete the selected employee.
        """
        employee = Employees.query.get(employee_id)
        session.delete(employee)
        session.commit()
        result = employee_schema.dump(employee)
        return jsonify(result)


class EmployeesResource(Resource):
    """
    Implementation of methods that do not require specification.
    """

    def get(self):
        """
        Get all employees in the database.
        """
        employees = Employees.query.all()
        return employees_schema.jsonify(employees)


    def post(self):
        """
        Add a employee in the database.
        """
        employee_name = request.json['employee_name']
        employee_role = request.json['employee_role']
        employee_salary = request.json['employee_salary']

        new_employee = Employees(employee_name, employee_role, employee_salary)

        session.add(new_employee)
        session.commit()

        result = employee_schema.dump(new_employee)
        return jsonify(result)


class SnackResource(Resource):
    """
    Implementation of specific snack manipulation methods defined by snack_id.
    """

    def get(self, snack_id):
        """
        Get a specific snack in the database.
        """
        snack = SnackMenu.query.get(snack_id)
        return snack_schema.jsonify(snack)


    def put(self, snack_id):
        """
        Updates the snack data.
        """
        snack = SnackMenu.query.get(snack_id)

        snack.snack_name = request.json['snack_name']
        snack.snack_price = request.json['snack_price']

        result = snack_schema.dump(snack)

        session.commit()
        return jsonify(result)


    def delete(self, snack_id):
        """
        Delete the selected snack.
        """
        snack = SnackMenu.query.get(snack_id)
        session.delete(snack)
        session.commit()
        result = snack_schema.dump(snack)
        return jsonify(result)


class SnacksResource(Resource):
    """
    Implementation of methods that do not require specification.
    """

    def get(self):
        """
        Get all snacks in the database.
        """
        snacks = SnackMenu.query.all()
        return snacks_schema.jsonify(snacks)


    def post(self):
        """
        Add a employee in the database.
        """
        snack_name = request.json['snack_name']
        snack_price = request.json['snack_price']

        new_snack = SnackMenu(snack_name, snack_price)

        session.add(new_snack)
        session.commit()

        result = snacks_schema.dump(new_snack)
        return jsonify(result)


# employees routes
api.add_resource(EmployeeResource, '/employees/<int:employee_id>')
api.add_resource(EmployeesResource, '/employees')

# snacks routes
api.add_resource(SnackResource, '/snacks/<int:snack_id>')
api.add_resource(SnacksResource, '/snacks')
