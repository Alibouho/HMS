from models.db import db

class Medicine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medicine_name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    expiry_date = db.Column(db.String(20))