from models.db import db
from models.models_task import Task

def add_task_service(data):
    task = Task(
        task_title=data["task_title"],
        description=data["description"],
        assigned_date=data["assigned_date"],
        status=data["status"]
    )

    db.session.add(task)
    db.session.commit()