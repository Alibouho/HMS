from models.db import db

class PatientBill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    bill_date = db.Column(db.String(20))
    payment_status = db.Column(db.String(50))


class OperationalBill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bill_type = db.Column(db.String(100))
    amount = db.Column(db.Float)
    bill_date = db.Column(db.String(20))
    description = db.Column(db.String(200))