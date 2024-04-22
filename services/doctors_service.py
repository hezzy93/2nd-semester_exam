from fastapi import HTTPException
from schemas.doctors_schema import doctors, DoctorsCreateEdit, Doctors, DoctorsAvalability

class DoctorService:

    @staticmethod
    def parse_doctors(doctor_data):
        data = []
        for doc in doctor_data:
            data.append(doctors[doc])
        return data
    

    @staticmethod
    def get_doctor_by_id(doctor_id):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(detail='Doctor not found.', status_code=404)   
        return doctors[doctor_id]
    
    
    @staticmethod
    def create_doctor(doctor_data: DoctorsCreateEdit):
        id = len(doctors) +1
        doctor = Doctors(
            id=id,
            **doctor_data.model_dump()
            )
        doctors[id] = doctor
        return doctor
        

    @staticmethod
    def edit_doctor(doctor_id: int, payload: DoctorsCreateEdit):
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
        
        

    @staticmethod
    def doctor_avalability(doctor_id: int, payload: DoctorsAvalability):
        if doctor_id in doctors:
            doctor = doctors[doctor_id]
            # Update doctor attributes based on payload
            doctor.is_available = payload.is_available
            return doctor
        else:
            raise HTTPException(detail='Doctor not found.', status_code=404)
        

    @staticmethod
    def delete_doctor(doctor_id: int):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(detail='Doctor not found', status_code=404)
        del doctors[doctor_id]