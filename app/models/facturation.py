
from sqlalchemy import Column, Integer, Float, Date, ForeignKey, JSON, String
from sqlalchemy.orm import relationship
from app.db.session import Base

class Facturation(Base):
    __tablename__ = 'facturation'

    id = Column(Integer, primary_key=True, index=True)
    ordonnance_id = Column(Integer, ForeignKey('ordonnance.id'), nullable=True)  # Nullable
    patient_id = Column(Integer, ForeignKey('patient.id'))  # Lien avec Patient
    date_facturation = Column(Date)
    montant = Column(Float)
    statut_facturation = Column(String)
    medicaments_delivres = Column(JSON)
    unites_delivrees = Column(JSON)

    ordonnance = relationship("Ordonnance", back_populates="facturations")
    patient = relationship("Patient", back_populates="facturations")  # Nouvelle relation avec Patient
