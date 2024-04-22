from pydantic import BaseModel

class Patients(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: float
    height:float
    phone: int

class PatientsCreateEdit(BaseModel):
    name: str
    age: int
    sex: str
    weight: float
    height:float
    phone: int

patients: dict[int, Patients] = {
    0:  Patients(
        id=0, name='patient 1', age=45, sex='male', weight=56, height= 7.6, phone='08166834'
    ),
    1:  Patients(
     id=1, name='patient 2', age=50, sex='femalemale', weight=67, height= 7.6, phone='08166875'
    ),
    2:  Patients(
     id=2, name='patient 3', age=49, sex='male', weight=59, height= 7.6, phone='08166983'
    ),
}