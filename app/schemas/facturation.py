
from pydantic import BaseModel
from typing import Optional, List, Dict

class FacturationBase(BaseModel):
    ordonnance_id: int
    date_facturation: str
    montant: float
    statut_facturation: Optional[str] = None
    medicaments_delivres: Optional[List[Dict]] = None
    unites_delivrees: Optional[List[Dict]] = None

class FacturationCreate(FacturationBase):
    pass

class Facturation(FacturationBase):
    id: int

    class Config:
        orm_mode = True
