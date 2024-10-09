
from pydantic import BaseModel

class PatientMutuelleBase(BaseModel):
    patient_id: int
    mutuelle_id: int
    numero_securite_sociale: str
    taux_remboursement_65: float
    taux_remboursement_30: float
    taux_remboursement_15: float

class PatientMutuelleCreate(PatientMutuelleBase):
    pass

class PatientMutuelle(PatientMutuelleBase):
    id: int

    class Config:
        orm_mode = True

class PatientMutuelleCreate(PatientMutuelleBase):
    pass

class PatientMutuelle(PatientMutuelleBase):
    id: int

    class Config:
        orm_mode = True
