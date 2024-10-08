
from sqlalchemy import Column, Integer, ForeignKey, Float, String
from app.db.session import Base

class PatientMutuelle(Base):
    __tablename__ = 'patient_mutuelle'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    mutuelle_id = Column(Integer, ForeignKey('mutuelle.id'))
    numero_securite_sociale = Column(String)
    taux_remboursement_65 = Column(Float)
    taux_remboursement_30 = Column(Float)
    taux_remboursement_15 = Column(Float)
