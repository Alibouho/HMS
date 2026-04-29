from flask import Flask, render_template, request
from models.models_patient import Patient, db 
from services.services_patient import add_patient_service

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def base():
    return render_template("base.html")

@app.route('/add_patient', methods=["GET", "POST"])
def add_patient():

    if request.method == "POST":

        data = {
            "name":    request.form["name"],
            "age":     request.form["age"],
            "phone":   request.form["phone"],
            "address": request.form["address"]
        }

        add_patient_service(data)

        return "DATA SAVED SUCCESSFULLY"
        
    return render_template("add_patient.html")

@app.route('/view_update_patient')
def view_update_patient():

    patients = Patient.query.all()

    return render_template("view_update_patient.html", patients=patients)

@app.route('/edit_patient/<int:id>', methods=["GET", "POST"])
def edit_patient(id):

    patient = Patient.query.get(id)

    if request.method == "POST":

        patient.name = request.form["name"]
        patient.age = request.form["age"]
        patient.phone = request.form["phone"]
        patient.address = request.form["address"]

        db.session.commit()

        return "UPDATED SUCCESSFULLY"
        
    return render_template("edit_patient.html", patient=patient)

if __name__=='__main__':
    app.run(debug=True)


