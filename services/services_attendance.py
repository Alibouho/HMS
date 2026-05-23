from models.db import db
from models.models_attendance import Attendance

def add_attendance_service(data):
    attendance = Attendance(
        date=data["date"],
        check_in_time=data["check_in_time"],
        check_out_time=data["check_out_time"],
        status=data["status"],
        employee_id=data.get("employee_id")
    )

    db.session.add(attendance)
    db.session.commit()