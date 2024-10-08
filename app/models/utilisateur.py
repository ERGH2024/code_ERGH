
from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Utilisateur(Base):
    __tablename__ = 'utilisateur'

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    prenom = Column(String, index=True)
    role = Column(String)
    email = Column(String, unique=True)
    mot_de_passe = Column(String)
    code_simple = Column(String)
    mode_authentification = Column(String)
