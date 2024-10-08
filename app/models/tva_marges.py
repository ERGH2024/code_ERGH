
from sqlalchemy import Column, Integer, Float, String
from app.db.session import Base

class TVAMarges(Base):
    __tablename__ = 'tva_marges'

    id = Column(Integer, primary_key=True, index=True)
    taux_tva = Column(Float)
    categorie = Column(String)
    coef_marge = Column(Float)
