from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.dependency import get_db
from .. import models
from app.schemas import produit as schemas_produit

router = APIRouter(
    prefix="/produit",  # Changement pour utiliser le singulier
    tags=["Produit"]    # Utilisation du singulier ici aussi
)

# Créer un produit
@router.post("/", response_model=schemas_produit.Produit)
def create_produit(produit: schemas_produit.ProduitCreate, db: Session = Depends(get_db)):
    db_produit = models.Produit(
        nom_produit=produit.nom_produit,
        prix=produit.prix,
        description=produit.description,
        est_medicament=produit.est_medicament,
        quantite_stock=produit.quantite_stock,
        taux_tva_id=produit.taux_tva_id
    )
    db.add(db_produit)
    db.commit()
    db.refresh(db_produit)
    return db_produit

# Récupérer tous les produits
@router.get("/", response_model=List[schemas_produit.Produit])
def get_produits(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    produits = db.query(models.Produit).offset(skip).limit(limit).all()
    return produits

# Récupérer un produit par ID
@router.get("/{produit_id}", response_model=schemas_produit.Produit)
def get_produit(produit_id: int, db: Session = Depends(get_db)):
    produit = db.query(models.Produit).filter(models.Produit.id == produit_id).first()
    if not produit:
        raise HTTPException(status_code=404, detail="Produit not found")
    return produit

# Mettre à jour un produit
@router.put("/{produit_id}", response_model=schemas_produit.Produit)
def update_produit(produit_id: int, produit: schemas_produit.ProduitCreate, db: Session = Depends(get_db)):
    db_produit = db.query(models.Produit).filter(models.Produit.id == produit_id).first()
    if not db_produit:
        raise HTTPException(status_code=404, detail="Produit not found")

    db_produit.nom_produit = produit.nom_produit
    db_produit.prix = produit.prix
    db_produit.description = produit.description
    db_produit.est_medicament = produit.est_medicament
    db_produit.quantite_stock = produit.quantite_stock
    db_produit.taux_tva_id = produit.taux_tva_id

    db.commit()
    db.refresh(db_produit)
    return db_produit

# Supprimer un produit
@router.delete("/{produit_id}", response_model=schemas_produit.Produit)
def delete_produit(produit_id: int, db: Session = Depends(get_db)):
    db_produit = db.query(models.Produit).filter(models.Produit.id == produit_id).first()
    if not db_produit:
        raise HTTPException(status_code=404, detail="Produit not found")

    db.delete(db_produit)
    db.commit()
    return db_produit
