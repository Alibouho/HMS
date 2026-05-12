from models.db import db
from models.models_patient import Patient

def add_patient_service(data):

    patient = Patient(
        name=data["name"],
        age=data["age"],
        phone=data["phone"],
        address=data["address"]
    )

    db.session.add(patient)
    db.session.commit()
