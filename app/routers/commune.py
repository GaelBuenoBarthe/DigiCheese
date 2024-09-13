from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.schemas import commune as schemas
from app.infrastructure.api.client import commune as crud

router = APIRouter()

@router.post("/communes/", response_model=schemas.Commune)
def create_commune(commune: schemas.CommuneCreate, db: Session = Depends(SessionLocal)):
    return crud.create_commune(db=db, commune=commune)

@router.get("/communes/", response_model=List[schemas.Commune])
def read_communes(skip: int = 0, limit: int = 10, db: Session = Depends(SessionLocal)):
    return crud.get_communes(db, skip=skip, limit=limit)

@router.get("/communes/{commune_id}", response_model=schemas.Commune)
def read_commune(commune_id: int, db: Session = Depends(SessionLocal)):
    db_commune = crud.get_commune(db, commune_id=commune_id)
    if db_commune is None:
        raise HTTPException(status_code=404, detail="Commune not found")
    return db_commune

@router.put("/communes/{commune_id}", response_model=schemas.Commune)
def update_commune(commune_id: int, commune: schemas.CommuneUpdate, db: Session = Depends(SessionLocal)):
    return crud.update_commune(db=db, commune_id=commune_id, commune=commune)

@router.delete("/communes/{commune_id}", response_model=schemas.Commune)
def delete_commune(commune_id: int, db: Session = Depends(SessionLocal)):
    return crud.delete_commune(db=db, commune_id=commune_id)