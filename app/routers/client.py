from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.schemas import client as schemas
from app.infrastructure.api.client import client as crud

router = APIRouter()

@router.post("/clients/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(SessionLocal)):
    return crud.create_client(db=db, client=client)

@router.get("/clients/", response_model=List[schemas.Client])
def read_clients(skip: int = 0, limit: int = 10, db: Session = Depends(SessionLocal)):
    return crud.get_clients(db, skip=skip, limit=limit)

@router.get("/clients/{client_id}", response_model=schemas.Client)
def read_client(client_id: int, db: Session = Depends(SessionLocal)):
    db_client = crud.get_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

@router.put("/clients/{client_id}", response_model=schemas.Client)
def update_client(client_id: int, client: schemas.ClientUpdate, db: Session = Depends(SessionLocal)):
    return crud.update_client(db=db, client_id=client_id, client=client)

@router.delete("/clients/{client_id}", response_model=schemas.Client)
def delete_client(client_id: int, db: Session = Depends(SessionLocal)):
    return crud.delete_client(db=db, client_id=client_id)