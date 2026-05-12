from flask import Blueprint, render_template, request, redirect, url_for
from models.models_task import Task
from models.db import db
from services.services_task import add_task_service

task_bp = Blueprint('task', __name__)

# ---------------- TASK ----------------
@task_bp.route('/add_task', methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        data = {
            "task_title": request.form["task_title"],
            "description": request.form["description"],
            "assigned_date": request.form["assigned_date"],
            "status": request.form["status"]
        }
        add_task_service(data)
        return redirect(url_for('task.view_update_task'))
    return render_template("add_task.html")

@task_bp.route('/view_update_task')
def view_update_task():
    return render_template("view_update_task.html", tasks=Task.query.all())

@task_bp.route('/edit_task/<int:id>', methods=["GET", "POST"])
def edit_task(id):
    task = Task.query.get_or_404(id)
    if request.method == "POST":
        task.task_title = request.form["task_title"]
        task.description = request.form["description"]
        task.assigned_date = request.form["assigned_date"]
        task.status = request.form["status"]
        db.session.commit()
        return redirect(url_for('task.view_update_task'))
    return render_template("edit_task.html", task=task)