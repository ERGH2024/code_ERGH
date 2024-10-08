
from pydantic import BaseModel
from datetime import date
from typing import Optional, List, Dict

class OrdonnanceBase(BaseModel):
    date_emission_medecin: date
    date_prise_en_charge: Optional[date] = None
    duree_validite: Optional[int] = None
    nombre_utilisations: Optional[int] = None
    medecin: str
    type_ordonnance: str
    medicaments: Optional[List[Dict]] = None
    statut: Optional[str] = None
    statut_facturation: Optional[str] = None

class OrdonnanceCreate(OrdonnanceBase):
    patient_id: int

class Ordonnance(OrdonnanceBase):
    id: int

    class Config:
        orm_mode = True
