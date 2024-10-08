
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependency import get_db
from app.models.journal_activites import JournalActivites as JournalActivitesModel
from app.schemas.journal_activites import JournalActivites, JournalActivitesCreate

router = APIRouter()

@router.post("/journal_activites/", response_model=JournalActivites)
def create_journal_activites(journal_activites: JournalActivitesCreate, db: Session = Depends(get_db)):
    db_journal_activites = JournalActivitesModel(**journal_activites.dict())
    db.add(db_journal_activites)
    db.commit()
    db.refresh(db_journal_activites)
    return db_journal_activites

@router.get("/journal_activites/", response_model=list[JournalActivites])
def read_journal_activites(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(JournalActivitesModel).offset(skip).limit(limit).all()

@router.get("/journal_activites/{journal_activites_id}", response_model=JournalActivites)
def read_journal_activites(journal_activites_id: int, db: Session = Depends(get_db)):
    journal_activites = db.query(JournalActivitesModel).filter(JournalActivitesModel.id == journal_activites_id).first()
    if journal_activites is None:
        raise HTTPException(status_code=404, detail="JournalActivites not found")
    return journal_activites

@router.put("/journal_activites/{journal_activites_id}", response_model=JournalActivites)
def update_journal_activites(journal_activites_id: int, updated_journal_activites: JournalActivitesCreate, db: Session = Depends(get_db)):
    db_journal_activites = db.query(JournalActivitesModel).filter(JournalActivitesModel.id == journal_activites_id).first()
    if db_journal_activites is None:
        raise HTTPException(status_code=404, detail="JournalActivites not found")
    for key, value in updated_journal_activites.dict().items():
        setattr(db_journal_activites, key, value)
    db.commit()
    return db_journal_activites

@router.delete("/journal_activites/{journal_activites_id}")
def delete_journal_activites(journal_activites_id: int, db: Session = Depends(get_db)):
    db_journal_activites = db.query(JournalActivitesModel).filter(JournalActivitesModel.id == journal_activites_id).first()
    if db_journal_activites is None:
        raise HTTPException(status_code=404, detail="JournalActivites not found")
    db.delete(db_journal_activites)
    db.commit()
    return {"detail": "JournalActivites deleted successfully"}
