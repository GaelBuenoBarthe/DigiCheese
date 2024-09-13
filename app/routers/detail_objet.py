from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud
from app.schemas.detail_objet import DetailObjet, DetailObjetCreate
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/detail_objets/", response_model=DetailObjet)
def create_detail_objet(detail_objet: DetailObjetCreate, db: Session = Depends(get_db)):
    return crud.create_detail_objet(db=db, detail_objet=detail_objet)

@router.get("/detail_objets/{id}", response_model=DetailObjet)
def read_detail_objet(id: int, db: Session = Depends(get_db)):
    db_detail_objet = crud.get_detail_objet(db, id=id)
    if db_detail_objet is None:
        raise HTTPException(status_code=404, detail="Detail objet non trouvé")
    return db_detail_objet

@router.get("/detail_objets/", response_model=List[DetailObjet])
def read_detail_objets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_detail_objets(db, skip=skip, limit=limit)

@router.put("/detail_objets/{id}", response_model=DetailObjet)
def update_detail_objet(id: int, detail_objet: DetailObjetCreate, db: Session = Depends(get_db)):
    return crud.update_detail_objet(db=db, id=id, detail_objet=detail_objet)

@router.delete("/detail_objets/{id}", response_model=DetailObjet)
def delete_detail_objet(id: int, db: Session = Depends(get_db)):
    return crud.delete_detail_objet(db=db, id=id)