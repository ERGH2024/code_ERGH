
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependency import get_db
from app.models.sessions_utilisateur import SessionsUtilisateur as SessionsUtilisateurModel
from app.schemas.sessions_utilisateur import SessionsUtilisateur, SessionsUtilisateurCreate

router = APIRouter()

@router.post("/sessions_utilisateurs/", response_model=SessionsUtilisateur)
def create_sessions_utilisateur(sessions_utilisateur: SessionsUtilisateurCreate, db: Session = Depends(get_db)):
    db_sessions_utilisateur = SessionsUtilisateurModel(**sessions_utilisateur.dict())
    db.add(db_sessions_utilisateur)
    db.commit()
    db.refresh(db_sessions_utilisateur)
    return db_sessions_utilisateur

@router.get("/sessions_utilisateurs/", response_model=list[SessionsUtilisateur])
def read_sessions_utilisateurs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(SessionsUtilisateurModel).offset(skip).limit(limit).all()

@router.get("/sessions_utilisateurs/{sessions_utilisateur_id}", response_model=SessionsUtilisateur)
def read_sessions_utilisateur(sessions_utilisateur_id: int, db: Session = Depends(get_db)):
    sessions_utilisateur = db.query(SessionsUtilisateurModel).filter(SessionsUtilisateurModel.id == sessions_utilisateur_id).first()
    if sessions_utilisateur is None:
        raise HTTPException(status_code=404, detail="SessionsUtilisateur not found")
    return sessions_utilisateur

@router.put("/sessions_utilisateurs/{sessions_utilisateur_id}", response_model=SessionsUtilisateur)
def update_sessions_utilisateur(sessions_utilisateur_id: int, updated_sessions_utilisateur: SessionsUtilisateurCreate, db: Session = Depends(get_db)):
    db_sessions_utilisateur = db.query(SessionsUtilisateurModel).filter(SessionsUtilisateurModel.id == sessions_utilisateur_id).first()
    if db_sessions_utilisateur is None:
        raise HTTPException(status_code=404, detail="SessionsUtilisateur not found")
    for key, value in updated_sessions_utilisateur.dict().items():
        setattr(db_sessions_utilisateur, key, value)
    db.commit()
    return db_sessions_utilisateur

@router.delete("/sessions_utilisateurs/{sessions_utilisateur_id}")
def delete_sessions_utilisateur(sessions_utilisateur_id: int, db: Session = Depends(get_db)):
    db_sessions_utilisateur = db.query(SessionsUtilisateurModel).filter(SessionsUtilisateurModel.id == sessions_utilisateur_id).first()
    if db_sessions_utilisateur is None:
        raise HTTPException(status_code=404, detail="SessionsUtilisateur not found")
    db.delete(db_sessions_utilisateur)
    db.commit()
    return {"detail": "SessionsUtilisateur deleted successfully"}
