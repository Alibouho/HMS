from models.db import db

class Bed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bed_number = db.Column(db.String(50))
    ward = db.Column(db.String(100))
    bed_type = db.Column(db.String(100))
    status = db.Column(db.String(50))