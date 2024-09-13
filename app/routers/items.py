from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter()

#Recuperation de la base de donnée
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Définition des routes "post" pour les items
@router.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item non trouvé")
    return item