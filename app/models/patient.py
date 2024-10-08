
from sqlalchemy import Column, Integer, String, Date
from app.db.session import Base

class Patient(Base):
    __tablename__ = 'patient'

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    prenom = Column(String, index=True)
    date_naissance = Column(Date)
    adresse = Column(String)
    telephone = Column(String)
    email = Column(String)
    amo = Column(String)
    code_securite_sociale = Column(String)
    code_ame = Column(String)
    amc = Column(String)
