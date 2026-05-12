from flask import Blueprint, render_template, request, redirect, url_for
from models.models_bed import Bed
from models.db import db
from services.services_bed import add_bed_service

bed_bp = Blueprint('bed', __name__)

# ---------------- BED MANAGEMENT ----------------
@bed_bp.route('/add_bed', methods=["GET", "POST"])
def add_bed():
    if request.method == "POST":
        data = request.form
        add_bed_service(data)
        return redirect(url_for('bed.view_update_bed'))
    return render_template("add_bed.html")

@bed_bp.route('/view_update_bed')
def view_update_bed():
    return render_template("view_update_bed.html", beds=Bed.query.all())

@bed_bp.route('/edit_bed/<int:id>', methods=["GET", "POST"])
def edit_bed(id):
    bed = Bed.query.get_or_404(id)
    if request.method == "POST":
        bed.bed_number = request.form["bed_number"]
        bed.ward = request.form["ward"]
        bed.bed_type = request.form["bed_type"]
        bed.status = request.form["status"]
        db.session.commit()
        return redirect(url_for('bed.view_update_bed'))
    return render_template("edit_bed.html", bed=bed)