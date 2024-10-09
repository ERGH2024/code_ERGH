
from pydantic import BaseModel
from typing import Optional

class MutuelleBase(BaseModel):
    nom: str
    code_teletransmission: str

class MutuelleCreate(MutuelleBase):
    pass

class Mutuelle(MutuelleBase):
    id: int

    class Config:
        orm_mode = True

class MutuelleCreate(MutuelleBase):
    pass

class Mutuelle(MutuelleBase):
    id: int

    class Config:
        orm_mode = True
