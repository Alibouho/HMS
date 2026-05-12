from models.db import db
from models.models_employee import Employee

def add_employee_service(data):
    employee = Employee(
        full_name=data["full_name"],
        role=data["role"],
        phone_number=data["phone_number"],
        email=data["email"],
        shift=data["shift"]
    )

    db.session.add(employee)
    db.session.commit()