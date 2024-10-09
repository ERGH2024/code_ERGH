from sqlalchemy import Boolean, Column, Integer, String, Float, Date, ForeignKey, Text
from app.db.session import Base
from sqlalchemy.orm import relationship


class Produit(Base):
    __tablename__ = 'produit'

    id = Column(Integer, primary_key=True, index=True)
    nom_produit = Column(String, nullable=False)
    prix = Column(Float, nullable=False)
    description = Column(Text)
    est_medicament = Column(Boolean, default=False, nullable=False)  # Champ ajouté
    quantite_stock = Column(Integer, nullable=False)
    taux_tva_id = Column(Integer, ForeignKey('tva_marges.id'))  # Lien vers la TVA
    taux_tva = relationship("TVAMarges", back_populates="produits")