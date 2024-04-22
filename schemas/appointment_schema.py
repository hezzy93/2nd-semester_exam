
from pydantic import BaseModel
from schemas.patient_schema import patients, Patients
from schemas.doctors_schema import doctors, Doctors



# Define the Appointments class before using it in the list comprehension
class Appointments(BaseModel):
    id: int
    patient: Patients
    doctor: Doctors
    date: str

class AppointmentsCreate(BaseModel):
    patient: int
    doctor: int
    date: str
    
appointments: list[Appointments] = [
    Appointments(
        id=0, patient=patients[0], doctor=doctors[0], date='date1'
    )
]
    

