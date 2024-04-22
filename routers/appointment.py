
from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from schemas.appointment_schema import AppointmentsCreate, appointments

from services.appointment_service import AppointmentService


appointment_router = APIRouter()


def check_token(token: str):
        if token != "secret":
            raise HTTPException(status_code=403, detail="Unauthorized")

        return f"Token: {token}"



@appointment_router.post('', status_code=201)
def create_appointment(payload: AppointmentsCreate, token: Annotated[str, Depends(check_token)]):
    data = AppointmentService.create_appointment(payload, token)
    return {'message': 'success', 'data': data}


@appointment_router.get('', status_code=200)
def get_appointments():
    return {'message': 'success', 'data': appointments}
