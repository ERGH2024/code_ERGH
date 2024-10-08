
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from app.db.session import Base

class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True, index=True)
    medicament_id = Column(Integer, ForeignKey('medicament.id'))
    quantite = Column(Integer)
    date_mouvement = Column(Date)
    raison = Column(String)
