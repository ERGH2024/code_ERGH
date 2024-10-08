
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependency import get_db
from app.models.mutuelle import Mutuelle as MutuelleModel
from app.schemas.mutuelle import Mutuelle, MutuelleCreate

router = APIRouter()

@router.post("/mutuelles/", response_model=Mutuelle)
def create_mutuelle(mutuelle: MutuelleCreate, db: Session = Depends(get_db)):
    db_mutuelle = MutuelleModel(**mutuelle.dict())
    db.add(db_mutuelle)
    db.commit()
    db.refresh(db_mutuelle)
    return db_mutuelle

@router.get("/mutuelles/", response_model=list[Mutuelle])
def read_mutuelles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(MutuelleModel).offset(skip).limit(limit).all()

@router.get("/mutuelles/{mutuelle_id}", response_model=Mutuelle)
def read_mutuelle(mutuelle_id: int, db: Session = Depends(get_db)):
    mutuelle = db.query(MutuelleModel).filter(MutuelleModel.id == mutuelle_id).first()
    if mutuelle is None:
        raise HTTPException(status_code=404, detail="Mutuelle not found")
    return mutuelle

@router.put("/mutuelles/{mutuelle_id}", response_model=Mutuelle)
def update_mutuelle(mutuelle_id: int, updated_mutuelle: MutuelleCreate, db: Session = Depends(get_db)):
    db_mutuelle = db.query(MutuelleModel).filter(MutuelleModel.id == mutuelle_id).first()
    if db_mutuelle is None:
        raise HTTPException(status_code=404, detail="Mutuelle not found")
    for key, value in updated_mutuelle.dict().items():
        setattr(db_mutuelle, key, value)
    db.commit()
    return db_mutuelle

@router.delete("/mutuelles/{mutuelle_id}")
def delete_mutuelle(mutuelle_id: int, db: Session = Depends(get_db)):
    db_mutuelle = db.query(MutuelleModel).filter(MutuelleModel.id == mutuelle_id).first()
    if db_mutuelle is None:
        raise HTTPException(status_code=404, detail="Mutuelle not found")
    db.delete(db_mutuelle)
    db.commit()
    return {"detail": "Mutuelle deleted successfully"}
