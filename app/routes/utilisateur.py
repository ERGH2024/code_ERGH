
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependency import get_db
from app.models.utilisateur import Utilisateur as UtilisateurModel
from app.schemas.utilisateur import Utilisateur, UtilisateurCreate

router = APIRouter()

@router.post("/utilisateurs/", response_model=Utilisateur)
def create_utilisateur(utilisateur: UtilisateurCreate, db: Session = Depends(get_db)):
    db_utilisateur = UtilisateurModel(**utilisateur.dict())
    db.add(db_utilisateur)
    db.commit()
    db.refresh(db_utilisateur)
    return db_utilisateur

@router.get("/utilisateurs/", response_model=list[Utilisateur])
def read_utilisateurs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(UtilisateurModel).offset(skip).limit(limit).all()

@router.get("/utilisateurs/{utilisateur_id}", response_model=Utilisateur)
def read_utilisateur(utilisateur_id: int, db: Session = Depends(get_db)):
    utilisateur = db.query(UtilisateurModel).filter(UtilisateurModel.id == utilisateur_id).first()
    if utilisateur is None:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return utilisateur

@router.put("/utilisateurs/{utilisateur_id}", response_model=Utilisateur)
def update_utilisateur(utilisateur_id: int, updated_utilisateur: UtilisateurCreate, db: Session = Depends(get_db)):
    db_utilisateur = db.query(UtilisateurModel).filter(UtilisateurModel.id == utilisateur_id).first()
    if db_utilisateur is None:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    for key, value in updated_utilisateur.dict().items():
        setattr(db_utilisateur, key, value)
    db.commit()
    return db_utilisateur

@router.delete("/utilisateurs/{utilisateur_id}")
def delete_utilisateur(utilisateur_id: int, db: Session = Depends(get_db)):
    db_utilisateur = db.query(UtilisateurModel).filter(UtilisateurModel.id == utilisateur_id).first()
    if db_utilisateur is None:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    db.delete(db_utilisateur)
    db.commit()
    return {"detail": "Utilisateur deleted successfully"}
