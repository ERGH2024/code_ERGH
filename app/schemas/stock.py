
from pydantic import BaseModel

class StockBase(BaseModel):
    medicament_id: int
    quantite: int
    date_entree: str
    date_sortie: str

class StockCreate(StockBase):
    pass

class Stock(StockBase):
    id: int

    class Config:
        orm_mode = True
