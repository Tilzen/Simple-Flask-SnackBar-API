"""
Definition of database table models.
"""
from app import db, marshmallow


class SnackMenu(db.Model):
    """
    Snack menu model.
    """
    __tablename__ = 'menu'

    snack_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    snack_name = db.Column(db.String)
    snack_price = db.Column(db.String)

    def __init__(self, snack_name, snack_price):
        self.snack_name = snack_name
        self.snack_price = snack_price

    def __repr__(self):
        return f'<Employee {self.snack_name}>'


class SnackMenuSchema(marshmallow.ModelSchema):
    class Meta:
        fields = ('snack_id', 'snack_name', 'snack_price')


class Employees(db.Model):
    """
    Employees model.
    """
    __tablename__ = 'employees'

    employee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employee_name = db.Column(db.String)
    employee_role = db.Column(db.String)
    employee_salary = db.Column(db.String)

    def __init__(self, employee_name, employee_role, employee_salary):
        self.employee_name = employee_name
        self.employee_role = employee_role
        self.employee_salary = employee_salary

    def __repr__(self):
        return f'<Employee {self.employee_name}>'


class EmployeesSchema(marshmallow.ModelSchema):
    class Meta:
        fields = ('employee_id', 'employee_name',
                  'employee_role', 'employee_salary')
