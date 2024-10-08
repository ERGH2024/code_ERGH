
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependency import get_db
from app.models.stock import Stock as StockModel
from app.schemas.stock import Stock, StockCreate

router = APIRouter()

@router.post("/stocks/", response_model=Stock)
def create_stock(stock: StockCreate, db: Session = Depends(get_db)):
    db_stock = StockModel(**stock.dict())
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock

@router.get("/stocks/", response_model=list[Stock])
def read_stocks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(StockModel).offset(skip).limit(limit).all()

@router.get("/stocks/{stock_id}", response_model=Stock)
def read_stock(stock_id: int, db: Session = Depends(get_db)):
    stock = db.query(StockModel).filter(StockModel.id == stock_id).first()
    if stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    return stock

@router.put("/stocks/{stock_id}", response_model=Stock)
def update_stock(stock_id: int, updated_stock: StockCreate, db: Session = Depends(get_db)):
    db_stock = db.query(StockModel).filter(StockModel.id == stock_id).first()
    if db_stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    for key, value in updated_stock.dict().items():
        setattr(db_stock, key, value)
    db.commit()
    return db_stock

@router.delete("/stocks/{stock_id}")
def delete_stock(stock_id: int, db: Session = Depends(get_db)):
    db_stock = db.query(StockModel).filter(StockModel.id == stock_id).first()
    if db_stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    db.delete(db_stock)
    db.commit()
    return {"detail": "Stock deleted successfully"}
