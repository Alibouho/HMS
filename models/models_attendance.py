from models.db import db

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20))
    check_in_time = db.Column(db.String(20))
    check_out_time = db.Column(db.String(20))
    status = db.Column(db.String(50))
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    employee = db.relationship('Employee', backref=db.backref('attendances', lazy=True))