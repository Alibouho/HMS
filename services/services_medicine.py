from models.db import db
from models.models_medicine import Medicine

def add_medicine_service(data):
    medicine = Medicine(
        medicine_name=data["medicine_name"],
        category=data["category"],
        quantity=data["quantity"],
        price=data["price"],
        expiry_date=data["expiry_date"]
    )

    db.session.add(medicine)
    db.session.commit()