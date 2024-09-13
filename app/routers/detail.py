from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.infrastructure.api.commande.detail import Detail as crud
from app.schemas.detail import Detail, DetailCreate
from app.database import SessionLocal

router = APIRouter()

#Creation d'une fonction pour obtenir la session de la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Définition des routes "post" pour les détails
@router.post("/details/", response_model=Detail)
def create_detail(detail: DetailCreate, db: Session = Depends(get_db)):
    return crud.create_detail(db=db, detail=detail)

#Définition des routes "get" pour les id de détails
@router.get("/details/{id}", response_model=Detail)
def read_detail(id: int, db: Session = Depends(get_db)):
    db_detail = crud.get_detail(db, id=id)
    if db_detail is None:
        raise HTTPException(status_code=404, detail="Detail non trouvé")
    return db_detail

#Définition des routes "get" pour les détails
@router.get("/details/", response_model=List[Detail])
def read_details(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_details(db, skip=skip, limit=limit)

#Définition des routes "put" pour les id de détails
@router.put("/details/{id}", response_model=Detail)
def update_detail(id: int, detail: DetailCreate, db: Session = Depends(get_db)):
    return crud.update_detail(db=db, id=id, detail=detail)

#Définition des routes "delete" pour les id de détails
@router.delete("/details/{id}", response_model=Detail)
def delete_detail(id: int, db: Session = Depends(get_db)):
    return crud.delete_detail(db=db, id=id)