from datetime import date
from pydantic import BaseModel
from typing import Optional, Dict

# Schéma de base pour une facturation
class FacturationBase(BaseModel):
    ordonnance_id: Optional[int] = None  # Optionnel
    patient_id: int  # Obligatoire
    date_facturation: date
    montant: float
    statut_facturation: str
    medicaments_delivrees: dict
    unites_delivrees: dict

# Schéma utilisé lors de la création d'une facturation (hérite de FacturationBase)
class FacturationCreate(FacturationBase):
    pass

# Schéma utilisé pour les réponses incluant l'ID et orm_mode activé
class Facturation(FacturationBase):
    id: int

    class Config:
        orm_mode = True  # Permet à Pydantic de fonctionner avec SQLAlchemy


