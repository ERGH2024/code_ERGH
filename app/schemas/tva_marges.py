
from pydantic import BaseModel

class TVAMargesBase(BaseModel):
    taux_tva: float
    categorie: str
    coef_marge: float

class TVAMargesCreate(TVAMargesBase):
    pass

class TVAMarges(TVAMargesBase):
    id: int

    class Config:
        orm_mode = True
