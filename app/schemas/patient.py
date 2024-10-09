
from pydantic import BaseModel
from datetime import date
from typing import Optional

class PatientBase(BaseModel):
    nom: str
    prenom: str
    date_naissance: date
    adresse: Optional[str] = None
    telephone: Optional[str] = None
    email: Optional[str] = None
    amo: Optional[str] = None
    code_securite_sociale: Optional[str] = None
    code_ame: Optional[str] = None
    amc: Optional[str] = None

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int

    class Config:
        orm_mode = True

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int

    class Config:
        orm_mode = True
