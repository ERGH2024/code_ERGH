
from pydantic import BaseModel

class UtilisateurBase(BaseModel):
    nom: str
    prenom: str
    role: str
    email: str
    mot_de_passe: str
    code_simple: str
    mode_authentification: str

class UtilisateurCreate(UtilisateurBase):
    pass

class Utilisateur(UtilisateurBase):
    id: int

    class Config:
        orm_mode = True
