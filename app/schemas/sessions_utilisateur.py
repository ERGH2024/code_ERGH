
from pydantic import BaseModel
from datetime import datetime

class SessionsUtilisateurBase(BaseModel):
    utilisateur_id: int
    date_debut: datetime
    date_fin: datetime

class SessionsUtilisateurCreate(SessionsUtilisateurBase):
    pass

class SessionsUtilisateur(SessionsUtilisateurBase):
    id: int

    class Config:
        orm_mode = True
