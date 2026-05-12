from models.db import db
from models.models_billing import PatientBill, OperationalBill

def add_patient_bill_service(data):
    bill = PatientBill(
        amount=data["amount"],
        bill_date=data["bill_date"],
        payment_status=data["payment_status"]
    )

    db.session.add(bill)
    db.session.commit()


def add_operational_bill_service(data):
    bill = OperationalBill(
        bill_type=data["bill_type"],
        amount=data["amount"],
        bill_date=data["bill_date"],
        description=data["description"]
    )

    db.session.add(bill)
    db.session.commit()