from flask import Flask, render_template, request, redirect, url_for

from models.db import db

from routes.routes_patient import patient_bp
from routes.routes_employee import employee_bp
from routes.routes_task import task_bp
from routes.routes_attendance import attendance_bp
from routes.routes_medicine import medicine_bp
from routes.routes_bed import bed_bp
from routes.routes_billing import billing_bp

from models.models_employee import Employee
from models.models_task import Task
from models.models_attendance import Attendance
from models.models_medicine import Medicine
from models.models_bed import Bed
from models.models_billing import PatientBill, OperationalBill

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(patient_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(task_bp)
app.register_blueprint(attendance_bp)
app.register_blueprint(medicine_bp)
app.register_blueprint(bed_bp)
app.register_blueprint(billing_bp)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def base():
    return render_template("base.html")


if __name__ == '__main__':
    app.run(debug=True)