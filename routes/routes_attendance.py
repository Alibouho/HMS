from flask import Blueprint, render_template, request, redirect, url_for
from models.models_attendance import Attendance
from models.db import db
from services.services_attendance import add_attendance_service

attendance_bp = Blueprint('attendance', __name__)

# ---------------- ATTENDANCE ----------------
@attendance_bp.route('/add_attendance', methods=["GET", "POST"])
def add_attendance():
    if request.method == "POST":
        data = {
            "date": request.form["date"],
            "check_in_time": request.form["check_in_time"],
            "check_out_time": request.form["check_out_time"],
            "status": request.form["status"]
        }
        add_attendance_service(data)
        return redirect(url_for('attendance.view_update_attendance'))
    return render_template("add_attendance.html")

@attendance_bp.route('/view_update_attendance')
def view_update_attendance():
    return render_template("view_update_attendance.html", attendances=Attendance.query.all())

@attendance_bp.route('/edit_attendance/<int:id>', methods=["GET", "POST"])
def edit_attendance(id):
    attendance = Attendance.query.get_or_404(id)
    if request.method == "POST":
        attendance.date = request.form["date"]
        attendance.check_in_time = request.form["check_in_time"]
        attendance.check_out_time = request.form["check_out_time"]
        attendance.status = request.form["status"]
        db.session.commit()
        return redirect(url_for('attendance.view_update_attendance'))
    return render_template("edit_attendance.html", attendance=attendance)