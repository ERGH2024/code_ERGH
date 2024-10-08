
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependency import get_db
from app.models.facturation import Facturation as FacturationModel
from app.schemas.facturation import Facturation, FacturationCreate

router = APIRouter()

@router.post("/facturations/", response_model=Facturation)
def create_facturation(facturation: FacturationCreate, db: Session = Depends(get_db)):
    db_facturation = FacturationModel(**facturation.dict())
    db.add(db_facturation)
    db.commit()
    db.refresh(db_facturation)
    return db_facturation

@router.get("/facturations/", response_model=list[Facturation])
def read_facturations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(FacturationModel).offset(skip).limit(limit).all()

@router.get("/facturations/{facturation_id}", response_model=Facturation)
def read_facturation(facturation_id: int, db: Session = Depends(get_db)):
    facturation = db.query(FacturationModel).filter(FacturationModel.id == facturation_id).first()
    if facturation is None:
        raise HTTPException(status_code=404, detail="Facturation not found")
    return facturation

@router.put("/facturations/{facturation_id}", response_model=Facturation)
def update_facturation(facturation_id: int, updated_facturation: FacturationCreate, db: Session = Depends(get_db)):
    db_facturation = db.query(FacturationModel).filter(FacturationModel.id == facturation_id).first()
    if db_facturation is None:
        raise HTTPException(status_code=404, detail="Facturation not found")
    for key, value in updated_facturation.dict().items():
        setattr(db_facturation, key, value)
    db.commit()
    return db_facturation

@router.delete("/facturations/{facturation_id}")
def delete_facturation(facturation_id: int, db: Session = Depends(get_db)):
    db_facturation = db.query(FacturationModel).filter(FacturationModel.id == facturation_id).first()
    if db_facturation is None:
        raise HTTPException(status_code=404, detail="Facturation not found")
    db.delete(db_facturation)
    db.commit()
    return {"detail": "Facturation deleted successfully"}
