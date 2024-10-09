from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.dependency import get_db
from app import models
from app.schemas import facturation as schemas_facturation  # Import correct depuis le fichier schemas/facturation.py


router = APIRouter(
    prefix="/facturation",
    tags=["Facturation"]
)

# Créer une facturation
@router.post("/", response_model=schemas_facturation.Facturation)
def create_facturation(facturation: schemas_facturation.FacturationCreate, db: Session = Depends(get_db)):
    db_facturation = models.Facturation(
        ordonnance_id=facturation.ordonnance_id,  # Peut être None
        patient_id=facturation.patient_id,  # Lien vers Patient
        date_facturation=facturation.date_facturation,
        montant=facturation.montant,
        statut_facturation=facturation.statut_facturation,
        medicaments_delivrees=facturation.medicaments_delivrees,
        unites_delivrees=facturation.unites_delivrees
    )
    db.add(db_facturation)
    db.commit()
    db.refresh(db_facturation)
    return db_facturation

# Récupérer toutes les facturations
@router.get("/", response_model=List[schemas_facturation.Facturation])
def get_facturations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    facturations = db.query(models.Facturation).offset(skip).limit(limit).all()
    return facturations

# Récupérer une facturation par ID
@router.get("/{facturation_id}", response_model=schemas_facturation.Facturation)
def get_facturation(facturation_id: int, db: Session = Depends(get_db)):
    facturation = db.query(models.Facturation).filter(models.Facturation.id == facturation_id).first()
    if not facturation:
        raise HTTPException(status_code=404, detail="Facturation not found")
    return facturation

# Mettre à jour une facturation
@router.put("/{facturation_id}", response_model=schemas_facturation.Facturation)
def update_facturation(facturation_id: int, facturation: schemas_facturation.FacturationCreate, db: Session = Depends(get_db)):
    db_facturation = db.query(models.Facturation).filter(models.Facturation.id == facturation_id).first()
    if not db_facturation:
        raise HTTPException(status_code=404, detail="Facturation not found")
    
    db_facturation.ordonnance_id = facturation.ordonnance_id
    db_facturation.patient_id = facturation.patient_id
    db_facturation.date_facturation = facturation.date_facturation
    db_facturation.montant = facturation.montant
    db_facturation.statut_facturation = facturation.statut_facturation
    db_facturation.medicaments_delivrees = facturation.medicaments_delivrees
    db_facturation.unites_delivrees = facturation.unites_delivrees

    db.commit()
    db.refresh(db_facturation)
    return db_facturation

# Supprimer une facturation
@router.delete("/{facturation_id}", response_model=schemas_facturation.Facturation)
def delete_facturation(facturation_id: int, db: Session = Depends(get_db)):
    db_facturation = db.query(models.Facturation).filter(models.Facturation.id == facturation_id).first()
    if not db_facturation:
        raise HTTPException(status_code=404, detail="Facturation not found")
    
    db.delete(db_facturation)
    db.commit()
    return db_facturation
