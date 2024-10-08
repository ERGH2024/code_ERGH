
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from app.db.session import Base

class Medicament(Base):
    __tablename__ = 'medicament'

    id = Column(Integer, primary_key=True, index=True)
    nom_commercial = Column(String, index=True)
    DCI = Column(String, index=True)
    dosage = Column(String)
    forme = Column(String)
    code_cis = Column(String)
    prix = Column(Float)
    unites_volume = Column(String)
    titulaire_amm = Column(String)
    taux_tva = Column(Float)
    date_expiration = Column(Date)
    description = Column(String)
