
from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey
from app.db.session import Base

class SessionsUtilisateur(Base):
    __tablename__ = 'sessions_utilisateur'

    id = Column(Integer, primary_key=True, index=True)
    utilisateur_id = Column(Integer, ForeignKey('utilisateur.id'))
    date_debut = Column(TIMESTAMP)
    date_fin = Column(TIMESTAMP)
