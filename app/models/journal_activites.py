
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from app.db.session import Base

class JournalActivites(Base):
    __tablename__ = 'journal_activites'

    id = Column(Integer, primary_key=True, index=True)
    utilisateur_id = Column(Integer, ForeignKey('utilisateur.id'))
    date_activite = Column(TIMESTAMP)
    type_activite = Column(String)
    description = Column(String)
