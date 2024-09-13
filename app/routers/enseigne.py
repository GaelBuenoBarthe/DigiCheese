from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.schemas import enseigne as schemas
from app.infrastructure.api.client import enseigne as crud

router = APIRouter()

@router.post("/enseignes/", response_model=schemas.Enseigne)
def create_enseigne(enseigne: schemas.EnseigneCreate, db: Session = Depends(SessionLocal)):
    return crud.create_enseigne(db=db, enseigne=enseigne)

@router.get("/enseignes/", response_model=List[schemas.Enseigne])
def read_enseignes(skip: int = 0, limit: int = 10, db: Session = Depends(SessionLocal)):
    return crud.get_enseignes(db, skip=skip, limit=limit)

@router.get("/enseignes/{enseigne_id}", response_model=schemas.Enseigne)
def read_enseigne(enseigne_id: int, db: Session = Depends(SessionLocal)):
    db_enseigne = crud.get_enseigne(db, enseigne_id=enseigne_id)
    if db_enseigne is None:
        raise HTTPException(status_code=404, detail="Enseigne not found")
    return db_enseigne

@router.put("/enseignes/{enseigne_id}", response_model=schemas.Enseigne)
def update_enseigne(enseigne_id: int, enseigne: schemas.EnseigneUpdate, db: Session = Depends(SessionLocal)):
    return crud.update_enseigne(db=db, enseigne_id=enseigne_id, enseigne=enseigne)

@router.delete("/enseignes/{enseigne_id}", response_model=schemas.Enseigne)
def delete_enseigne(enseigne_id: int, db: Session = Depends(SessionLocal)):
    return crud.delete_enseigne(db=db, enseigne_id=enseigne_id)