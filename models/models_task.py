from models.models_patient import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_title = db.Column(db.String(100))
    description = db.Column(db.String(200))
    assigned_date = db.Column(db.String(20))
    status = db.Column(db.String(50))