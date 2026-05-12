from flask import Blueprint, render_template, request, redirect, url_for
from models.models_medicine import Medicine
from models.db import db
from services.services_medicine import add_medicine_service

medicine_bp = Blueprint('medicine', __name__)

# ---------------- MEDICINE ----------------
@medicine_bp.route('/add_medicine', methods=["GET", "POST"])
def add_medicine():
    if request.method == "POST":
        data = request.form
        add_medicine_service(data)
        return redirect(url_for('medicine.view_update_medicine'))
    return render_template("add_medicine.html")

@medicine_bp.route('/view_update_medicine')
def view_update_medicine():
    return render_template("view_update_medicine.html", medicines=Medicine.query.all())

@medicine_bp.route('/edit_medicine/<int:id>', methods=["GET", "POST"])
def edit_medicine(id):
    medicine = Medicine.query.get_or_404(id)
    if request.method == "POST":
        medicine.medicine_name = request.form["medicine_name"]
        medicine.category = request.form["category"]
        medicine.quantity = request.form["quantity"]
        medicine.price = request.form["price"]
        medicine.expiry_date = request.form["expiry_date"]
        db.session.commit()
        return redirect(url_for('medicine.view_update_medicine'))
    return render_template("edit_medicine.html", medicine=medicine)