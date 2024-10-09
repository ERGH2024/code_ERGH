
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from app.db.session import Base
from sqlalchemy.orm import relationship

class Medicament(Base):
    __tablename__ = 'medicament'

    id = Column(Integer, primary_key=True, index=True)
    produit_id = Column(Integer, ForeignKey('produit.id'), nullable=False)  # Lien avec Produit
    DCI = Column(String)
    dosage = Column(String)
    forme = Column(String)
    code_cis = Column(String)
    unites_volume = Column(String)
    titulaire_amm = Column(String)
    date_expiration = Column(Date)
    
    produit = relationship("Produit", back_populates="medicament")

