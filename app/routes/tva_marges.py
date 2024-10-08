
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependency import get_db
from app.models.tva_marges import TVAMarges as TVAMargesModel
from app.schemas.tva_marges import TVAMarges, TVAMargesCreate

router = APIRouter()

@router.post("/tva_marges/", response_model=TVAMarges)
def create_tva_marges(tva_marges: TVAMargesCreate, db: Session = Depends(get_db)):
    db_tva_marges = TVAMargesModel(**tva_marges.dict())
    db.add(db_tva_marges)
    db.commit()
    db.refresh(db_tva_marges)
    return db_tva_marges

@router.get("/tva_marges/", response_model=list[TVAMarges])
def read_tva_marges(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(TVAMargesModel).offset(skip).limit(limit).all()

@router.get("/tva_marges/{tva_marges_id}", response_model=TVAMarges)
def read_tva_marges(tva_marges_id: int, db: Session = Depends(get_db)):
    tva_marges = db.query(TVAMargesModel).filter(TVAMargesModel.id == tva_marges_id).first()
    if tva_marges is None:
        raise HTTPException(status_code=404, detail="TVAMarges not found")
    return tva_marges

@router.put("/tva_marges/{tva_marges_id}", response_model=TVAMarges)
def update_tva_marges(tva_marges_id: int, updated_tva_marges: TVAMargesCreate, db: Session = Depends(get_db)):
    db_tva_marges = db.query(TVAMargesModel).filter(TVAMargesModel.id == tva_marges_id).first()
    if db_tva_marges is None:
        raise HTTPException(status_code=404, detail="TVAMarges not found")
    for key, value in updated_tva_marges.dict().items():
        setattr(db_tva_marges, key, value)
    db.commit()
    return db_tva_marges

@router.delete("/tva_marges/{tva_marges_id}")
def delete_tva_marges(tva_marges_id: int, db: Session = Depends(get_db)):
    db_tva_marges = db.query(TVAMargesModel).filter(TVAMargesModel.id == tva_marges_id).first()
    if db_tva_marges is None:
        raise HTTPException(status_code=404, detail="TVAMarges not found")
    db.delete(db_tva_marges)
    db.commit()
    return {"detail": "TVAMarges deleted successfully"}
