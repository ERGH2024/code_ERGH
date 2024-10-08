
from pydantic import BaseModel
from datetime import date
from typing import Optional

class MedicamentBase(BaseModel):
    nom_commercial: str
    DCI: str
    dosage: str
    forme: str
    code_cis: str
    prix: float
    unites_volume: Optional[str] = None
    titulaire_amm: Optional[str] = None
    taux_tva: Optional[float] = None
    date_expiration: Optional[date] = None
    description: Optional[str] = None

class MedicamentCreate(MedicamentBase):
    pass

class Medicament(MedicamentBase):
    id: int

    class Config:
        orm_mode = True
