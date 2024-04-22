from pydantic import BaseModel

class Doctors(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    is_available: bool

class DoctorsCreateEdit(BaseModel):
    name: str
    specialization: str
    phone: str
    is_available: bool  

class DoctorsAvalability(BaseModel):
    is_avaliable: bool


doctors: dict[int, Doctors] = {
    0:Doctors(
        id=0, name='doctor 1', specialization='surgery', phone='09277474', is_available=True
    ),

    1:Doctors(
        id=1, name='doctor 2', specialization='surgery', phone='09277474', is_available=True
    ),
    2:Doctors(
        id=2, name='doctor 2', specialization='surgery', phone='09277474', is_available=False
    ),
}





 