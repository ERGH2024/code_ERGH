from typing import Optional
from pydantic import BaseModel


class ProduitBase(BaseModel):
    nom_produit: str
    prix: float
    description: Optional[str] = None
    est_medicament: bool  # Nouveau champ
    quantite_stock: int
    taux_tva_id: int

class ProduitCreate(ProduitBase):
    pass

class Produit(ProduitBase):
    id: int

    class Config:
        orm_mode = True
