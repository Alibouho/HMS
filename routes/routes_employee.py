from flask import Blueprint, render_template, request, redirect, url_for
from models.models_employee import Employee
from models.db import db
from services.services_employee import add_employee_service

employee_bp = Blueprint('employee', __name__)

# ---------------- EMPLOYEE ----------------
@employee_bp.route('/add_employee', methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        data = {
            "full_name": request.form["full_name"],
            "role": request.form["role"],
            "phone_number": request.form["phone_number"],
            "email": request.form["email"],
        }
        add_employee_service(data)
        return redirect(url_for('employee.view_update_employee'))
    return render_template("add_employee.html")

@employee_bp.route('/view_update_employee')
def view_update_employee():
    return render_template("view_update_employee.html", employees=Employee.query.all())

@employee_bp.route('/edit_employee/<int:id>', methods=["GET", "POST"])
def edit_employee(id):
    employee = Employee.query.get_or_404(id)
    if request.method == "POST":
        employee.full_name = request.form["full_name"]
        employee.role = request.form["role"]
        employee.phone_number = request.form["phone_number"]
        employee.email = request.form["email"]
        db.session.commit()
        return redirect(url_for('employee.view_update_employee'))
    return render_template("edit_employee.html", employee=employee)