from flask import Blueprint, redirect, redirect, render_template, request, url_for
from models.models_patient import Patient
from models.db import db

from services.services_patient import add_patient_service
patient_bp = Blueprint('patient', __name__)


# ---------------- PATIENT ----------------
@patient_bp.route('/add_patient', methods=["GET", "POST"])
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


@patient_bp.route('/view_update_patient')
def view_update_patient():
    return render_template("view_update_patient.html", patients=Patient.query.all())


@patient_bp.route('/edit_patient/<int:id>', methods=["GET", "POST"])
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