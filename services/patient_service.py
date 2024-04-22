from fastapi import HTTPException
from schemas.patient_schema import patients, Patients, PatientsCreateEdit

class PatientService:

    @staticmethod
    def parse_patients(patient_data):
        data = []
        for pati in patient_data:
            data.append(patients[pati])
        return data
    
    @staticmethod
    def get_patient_by_id(patient_id):
        patient =patients.get(patient_id)
        if not patient:
            raise HTTPException(detail='Patient not found.', status_code=404)
        return patients[patient_id]
    
   
    @staticmethod
    def create_patient(patient_data: PatientsCreateEdit):
        id = len(patients) +1
        patient = Patients(
            id=id,
            **patient_data.model_dump()
        )
        patients[id] = patient
        return patient


    @staticmethod
    def edit_patient(patient_id: int, payload: PatientsCreateEdit):
        if patient_id in patients:
            patient = patients[patient_id]
            # Update patient attributes based on payload
            patient.name = payload.name
            patient.age = payload.age
            patient.phone = payload.phone
            patient.sex = payload.sex
            patient.weight = payload.weight
            patient.height = payload.height
            return patient
        else:
            raise HTTPException(detail='Patient not found.', status_code=404)
        

    @staticmethod
    def delete_patient(patient_id: int):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(detail='Customer not found.', status_code=404)
        del patients[patient_id]

