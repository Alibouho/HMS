from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
    id       =db.Column(db.Integer, primary_key=True)
    name     =db.Column(db.String(100))
    age      =db.Column(db.Integer)
    phone    =db.Column(db.String(20))
    address  =db.Column(db.String(200))

