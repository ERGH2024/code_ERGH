
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependency import get_db
from app.models.medicament import Medicament as MedicamentModel
from app.schemas.medicament import Medicament, MedicamentCreate

router = APIRouter()

@router.post("/medicaments/", response_model=Medicament)
def create_medicament(medicament: MedicamentCreate, db: Session = Depends(get_db)):
    db_medicament = MedicamentModel(**medicament.dict())
    db.add(db_medicament)
    db.commit()
    db.refresh(db_medicament)
    return db_medicament

@router.get("/medicaments/", response_model=list[Medicament])
def read_medicaments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(MedicamentModel).offset(skip).limit(limit).all()

@router.get("/medicaments/{medicament_id}", response_model=Medicament)
def read_medicament(medicament_id: int, db: Session = Depends(get_db)):
    medicament = db.query(MedicamentModel).filter(MedicamentModel.id == medicament_id).first()
    if medicament is None:
        raise HTTPException(status_code=404, detail="Medicament not found")
    return medicament

@router.put("/medicaments/{medicament_id}", response_model=Medicament)
def update_medicament(medicament_id: int, updated_medicament: MedicamentCreate, db: Session = Depends(get_db)):
    db_medicament = db.query(MedicamentModel).filter(MedicamentModel.id == medicament_id).first()
    if db_medicament is None:
        raise HTTPException(status_code=404, detail="Medicament not found")
    for key, value in updated_medicament.dict().items():
        setattr(db_medicament, key, value)
    db.commit()
    return db_medicament

@router.delete("/medicaments/{medicament_id}")
def delete_medicament(medicament_id: int, db: Session = Depends(get_db)):
    db_medicament = db.query(MedicamentModel).filter(MedicamentModel.id == medicament_id).first()
    if db_medicament is None:
        raise HTTPException(status_code=404, detail="Medicament not found")
    db.delete(db_medicament)
    db.commit()
    return {"detail": "Medicament deleted successfully"}
