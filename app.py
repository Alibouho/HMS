from flask import Flask, render_template, request, redirect, url_for

from models.models_patient import Patient, db
from models.models_task import Task
from models.models_billing import PatientBill, OperationalBill

from services.services_patient import add_patient_service
from services.services_task import add_task_service
from services.services_billing import add_patient_bill_service, add_operational_bill_service

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def base():
    return render_template("base.html")


# ---------------- PATIENT ----------------

@app.route('/add_patient', methods=["GET", "POST"])
def add_patient():
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "age": request.form["age"],
            "phone": request.form["phone"],
            "address": request.form["address"]
        }

        add_patient_service(data)
        return redirect(url_for('view_update_patient'))

    return render_template("add_patient.html")


@app.route('/view_update_patient')
def view_update_patient():
    patients = Patient.query.all()
    return render_template("view_update_patient.html", patients=patients)


@app.route('/edit_patient/<int:id>', methods=["GET", "POST"])
def edit_patient(id):
    patient = Patient.query.get_or_404(id)

    if request.method == "POST":
        patient.name = request.form["name"]
        patient.age = request.form["age"]
        patient.phone = request.form["phone"]
        patient.address = request.form["address"]

        db.session.commit()
        return redirect(url_for('view_update_patient'))

    return render_template("edit_patient.html", patient=patient)


# ---------------- TASK ----------------

@app.route('/add_task', methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        data = {
            "task_title": request.form["task_title"],
            "description": request.form["description"],
            "assigned_date": request.form["assigned_date"],
            "status": request.form["status"]
        }

        add_task_service(data)
        return redirect(url_for('view_update_task'))

    return render_template("add_task.html")


@app.route('/view_update_task')
def view_update_task():
    tasks = Task.query.all()
    return render_template("view_update_task.html", tasks=tasks)


@app.route('/edit_task/<int:id>', methods=["GET", "POST"])
def edit_task(id):
    task = Task.query.get_or_404(id)

    if request.method == "POST":
        task.task_title = request.form["task_title"]
        task.description = request.form["description"]
        task.assigned_date = request.form["assigned_date"]
        task.status = request.form["status"]

        db.session.commit()
        return redirect(url_for('view_update_task'))

    return render_template("edit_task.html", task=task)


# ---------------- PATIENT BILL ----------------

@app.route('/add_patient_bill', methods=["GET", "POST"])
def add_patient_bill():
    if request.method == "POST":
        data = {
            "amount": request.form["amount"],
            "bill_date": request.form["bill_date"],
            "payment_status": request.form["payment_status"]
        }

        add_patient_bill_service(data)
        return redirect(url_for('view_update_patient_bill'))

    return render_template("add_patient_bill.html")


@app.route('/view_update_patient_bill')
def view_update_patient_bill():
    bills = PatientBill.query.all()
    return render_template("view_update_patient_bill.html", bills=bills)


@app.route('/edit_patient_bill/<int:id>', methods=["GET", "POST"])
def edit_patient_bill(id):
    bill = PatientBill.query.get_or_404(id)

    if request.method == "POST":
        bill.amount = request.form["amount"]
        bill.bill_date = request.form["bill_date"]
        bill.payment_status = request.form["payment_status"]

        db.session.commit()
        return redirect(url_for('view_update_patient_bill'))

    return render_template("edit_patient_bill.html", bill=bill)


# ---------------- OPERATIONAL BILL ----------------

@app.route('/add_operational_bill', methods=["GET", "POST"])
def add_operational_bill():
    if request.method == "POST":
        data = {
            "bill_type": request.form["bill_type"],
            "amount": request.form["amount"],
            "bill_date": request.form["bill_date"],
            "description": request.form["description"]
        }

        add_operational_bill_service(data)
        return redirect(url_for('view_update_operational_bill'))

    return render_template("add_operational_bill.html")


@app.route('/view_update_operational_bill')
def view_update_operational_bill():
    bills = OperationalBill.query.all()
    return render_template("view_update_operational_bill.html", bills=bills)


@app.route('/edit_operational_bill/<int:id>', methods=["GET", "POST"])
def edit_operational_bill(id):
    bill = OperationalBill.query.get_or_404(id)

    if request.method == "POST":
        bill.bill_type = request.form["bill_type"]
        bill.amount = request.form["amount"]
        bill.bill_date = request.form["bill_date"]
        bill.description = request.form["description"]

        db.session.commit()
        return redirect(url_for('view_update_operational_bill'))

    return render_template("edit_operational_bill.html", bill=bill)


if __name__ == '__main__':
    app.run(debug=True)