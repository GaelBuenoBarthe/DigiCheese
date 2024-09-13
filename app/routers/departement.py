from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.schemas import departement as schemas
from app.infrastructure.api.client import departement as crud

router = APIRouter()

@router.post("/departements/", response_model=schemas.Departement)
def create_departement(departement: schemas.DepartementCreate, db: Session = Depends(SessionLocal)):
    return crud.create_departement(db=db, departement=departement)

@router.get("/departements/", response_model=List[schemas.Departement])
def read_departements(skip: int = 0, limit: int = 10, db: Session = Depends(SessionLocal)):
    return crud.get_departements(db, skip=skip, limit=limit)

@router.get("/departements/{departement_id}", response_model=schemas.Departement)
def read_departement(departement_id: int, db: Session = Depends(SessionLocal)):
    db_departement = crud.get_departement(db, departement_id=departement_id)
    if db_departement is None:
        raise HTTPException(status_code=404, detail="Departement not found")
    return db_departement

@router.put("/departements/{departement_id}", response_model=schemas.Departement)
def update_departement(departement_id: int, departement: schemas.DepartementUpdate, db: Session = Depends(SessionLocal)):
    return crud.update_departement(db=db, departement_id=departement_id, departement=departement)

@router.delete("/departements/{departement_id}", response_model=schemas.Departement)
def delete_departement(departement_id: int, db: Session = Depends(SessionLocal)):
    return crud.delete_departement(db=db, departement_id=departement_id)