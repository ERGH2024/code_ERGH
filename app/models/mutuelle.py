
from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Mutuelle(Base):
    __tablename__ = 'mutuelle'

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    code_teletransmission = Column(String)
