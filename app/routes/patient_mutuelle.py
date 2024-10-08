
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependency import get_db
from app.models.patient_mutuelle import PatientMutuelle as PatientMutuelleModel
from app.schemas.patient_mutuelle import PatientMutuelle, PatientMutuelleCreate

router = APIRouter()

@router.post("/patient_mutuelles/", response_model=PatientMutuelle)
def create_patient_mutuelle(patient_mutuelle: PatientMutuelleCreate, db: Session = Depends(get_db)):
    db_patient_mutuelle = PatientMutuelleModel(**patient_mutuelle.dict())
    db.add(db_patient_mutuelle)
    db.commit()
    db.refresh(db_patient_mutuelle)
    return db_patient_mutuelle

@router.get("/patient_mutuelles/", response_model=list[PatientMutuelle])
def read_patient_mutuelles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(PatientMutuelleModel).offset(skip).limit(limit).all()

@router.get("/patient_mutuelles/{patient_mutuelle_id}", response_model=PatientMutuelle)
def read_patient_mutuelle(patient_mutuelle_id: int, db: Session = Depends(get_db)):
    patient_mutuelle = db.query(PatientMutuelleModel).filter(PatientMutuelleModel.id == patient_mutuelle_id).first()
    if patient_mutuelle is None:
        raise HTTPException(status_code=404, detail="PatientMutuelle not found")
    return patient_mutuelle

@router.put("/patient_mutuelles/{patient_mutuelle_id}", response_model=PatientMutuelle)
def update_patient_mutuelle(patient_mutuelle_id: int, updated_patient_mutuelle: PatientMutuelleCreate, db: Session = Depends(get_db)):
    db_patient_mutuelle = db.query(PatientMutuelleModel).filter(PatientMutuelleModel.id == patient_mutuelle_id).first()
    if db_patient_mutuelle is None:
        raise HTTPException(status_code=404, detail="PatientMutuelle not found")
    for key, value in updated_patient_mutuelle.dict().items():
        setattr(db_patient_mutuelle, key, value)
    db.commit()
    return db_patient_mutuelle

@router.delete("/patient_mutuelles/{patient_mutuelle_id}")
def delete_patient_mutuelle(patient_mutuelle_id: int, db: Session = Depends(get_db)):
    db_patient_mutuelle = db.query(PatientMutuelleModel).filter(PatientMutuelleModel.id == patient_mutuelle_id).first()
    if db_patient_mutuelle is None:
        raise HTTPException(status_code=404, detail="PatientMutuelle not found")
    db.delete(db_patient_mutuelle)
    db.commit()
    return {"detail": "PatientMutuelle deleted successfully"}
