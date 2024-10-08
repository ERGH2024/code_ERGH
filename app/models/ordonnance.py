
from sqlalchemy import Column, Integer, String, Date, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.db.session import Base

class Ordonnance(Base):
    __tablename__ = 'ordonnance'

    id = Column(Integer, primary_key=True, index=True)
    date_emission_medecin = Column(Date)
    date_prise_en_charge = Column(Date)
    duree_validite = Column(Integer)
    nombre_utilisations = Column(Integer)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    medecin = Column(String)
    type_ordonnance = Column(String)
    medicaments = Column(JSON)
    statut = Column(String)
    statut_facturation = Column(String)

    patient = relationship("Patient", back_populates="ordonnances")
