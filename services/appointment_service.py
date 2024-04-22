from fastapi import HTTPException, Depends
from typing import Annotated

from schemas.appointment_schema import AppointmentsCreate, appointments, Appointments
from schemas.patient_schema import patients, Patients
from schemas.doctors_schema import doctors, Doctors, DoctorsAvalability

class AppointmentService:

    def check_token(self, token: str):
        if token != "secret":
            raise HTTPException(status_code=403, detail="Unauthorized")

        return f"Token: {token}"



    @staticmethod
    def doctor_availability(doctor_id: int, payload: DoctorsAvalability):
        if doctor_id in doctors:
            doctor = doctors[doctor_id]
            # Update doctor attributes based on payload
            doctor.name = payload.name
            doctor.specialization = payload.specialization
            doctor.phone = payload.phone
            doctor.is_available = payload.is_available
            return doctor
        else:
            raise HTTPException(detail='Doctor not found.', status_code=404)    