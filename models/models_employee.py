from models.db import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    role = db.Column(db.String(100))
    phone_number = db.Column(db.String(50))
    email = db.Column(db.String(100))
