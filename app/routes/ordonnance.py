
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependency import get_db
from app.models.ordonnance import Ordonnance as OrdonnanceModel
from app.schemas.ordonnance import Ordonnance, OrdonnanceCreate

router = APIRouter()

@router.post("/ordonnances/", response_model=Ordonnance)
def create_ordonnance(ordonnance: OrdonnanceCreate, db: Session = Depends(get_db)):
    db_ordonnance = OrdonnanceModel(**ordonnance.dict())
    db.add(db_ordonnance)
    db.commit()
    db.refresh(db_ordonnance)
    return db_ordonnance

@router.get("/ordonnances/", response_model=list[Ordonnance])
def read_ordonnances(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(OrdonnanceModel).offset(skip).limit(limit).all()

@router.get("/ordonnances/{ordonnance_id}", response_model=Ordonnance)
def read_ordonnance(ordonnance_id: int, db: Session = Depends(get_db)):
    ordonnance = db.query(OrdonnanceModel).filter(OrdonnanceModel.id == ordonnance_id).first()
    if ordonnance is None:
        raise HTTPException(status_code=404, detail="Ordonnance not found")
    return ordonnance

@router.put("/ordonnances/{ordonnance_id}", response_model=Ordonnance)
def update_ordonnance(ordonnance_id: int, updated_ordonnance: OrdonnanceCreate, db: Session = Depends(get_db)):
    db_ordonnance = db.query(OrdonnanceModel).filter(OrdonnanceModel.id == ordonnance_id).first()
    if db_ordonnance is None:
        raise HTTPException(status_code=404, detail="Ordonnance not found")
    for key, value in updated_ordonnance.dict().items():
        setattr(db_ordonnance, key, value)
    db.commit()
    return db_ordonnance

@router.delete("/ordonnances/{ordonnance_id}")
def delete_ordonnance(ordonnance_id: int, db: Session = Depends(get_db)):
    db_ordonnance = db.query(OrdonnanceModel).filter(OrdonnanceModel.id == ordonnance_id).first()
    if db_ordonnance is None:
        raise HTTPException(status_code=404, detail="Ordonnance not found")
    db.delete(db_ordonnance)
    db.commit()
    return {"detail": "Ordonnance deleted successfully"}
