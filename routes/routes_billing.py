from flask import Blueprint, render_template, request, redirect, url_for
from models.models_billing import PatientBill, OperationalBill
from models.db import db
from services.services_billing import add_patient_bill_service, add_operational_bill_service

billing_bp = Blueprint('billing', __name__)

# ---------------- BILLING ----------------
@billing_bp.route('/add_patient_bill', methods=["GET", "POST"])
def add_patient_bill():
    if request.method == "POST":
        add_patient_bill_service(request.form)
        return redirect(url_for('billing.view_update_patient_bill'))
    return render_template("add_patient_bill.html")

@billing_bp.route('/view_update_patient_bill')
def view_update_patient_bill():
    return render_template("view_update_patient_bill.html", bills=PatientBill.query.all())

@billing_bp.route('/edit_patient_bill/<int:id>', methods=["GET", "POST"])
def edit_patient_bill(id):
    bill = PatientBill.query.get_or_404(id)
    if request.method == "POST":
        bill.amount = request.form["amount"]
        bill.bill_date = request.form["bill_date"]
        bill.payment_status = request.form["payment_status"]
        db.session.commit()
        return redirect(url_for('billing.view_update_patient_bill'))
    return render_template("edit_patient_bill.html", bill=bill)

@billing_bp.route('/add_operational_bill', methods=["GET", "POST"])
def add_operational_bill():
    if request.method == "POST":
        add_operational_bill_service(request.form)
        return redirect(url_for('billing.view_update_operational_bill'))
    return render_template("add_operational_bill.html")

@billing_bp.route('/view_update_operational_bill')
def view_update_operational_bill():
    return render_template("view_update_operational_bill.html", bills=OperationalBill.query.all())

@billing_bp.route('/edit_operational_bill/<int:id>', methods=["GET", "POST"])
def edit_operational_bill(id):
    bill = OperationalBill.query.get_or_404(id)
    if request.method == "POST":
        bill.bill_type = request.form["bill_type"]
        bill.amount = request.form["amount"]
        bill.bill_date = request.form["bill_date"]
        bill.description = request.form["description"]
        db.session.commit()
        return redirect(url_for('billing.view_update_operational_bill'))
    return render_template("edit_operational_bill.html", bill=bill)