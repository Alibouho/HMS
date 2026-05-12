from models.db import db 
from models.models_bed import Bed

def add_bed_service(data):
    bed = Bed(
        bed_number=data["bed_number"],
        ward=data["ward"],
        bed_type=data["bed_type"],
        status=data["status"]
    )

    db.session.add(bed)
    db.session.commit()