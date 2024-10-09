
from pydantic import BaseModel
from typing import Optional, List, Dict

class FacturationBase(BaseModel):
    ordonnance_id: Optional[int] = None  # Optionnel
    patient_id: int  # Obligatoire
    date_facturation: date
    montant: float
    statut_facturation: str
    medicaments_delivrees: dict
    unites_delivrees: dict

