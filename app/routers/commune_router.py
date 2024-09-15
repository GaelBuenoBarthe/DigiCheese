from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.commune import CommuneCreate, CommuneUpdate, CommuneResponse
from app.infrastructure.api.client.commune_controller import (
    get_commune, get_all_communes, delete_commune, create_commune, update_commune
)

router = APIRouter()

@router.get("/", response_model=List[CommuneResponse])
def read_communes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[CommuneResponse]:
    return get_all_communes(skip, limit, db)

@router.post("/", response_model=CommuneResponse, status_code=201)
def create_commune(commune: CommuneCreate, db: Session = Depends(get_db)) -> CommuneResponse:
    return create_commune(commune, db)

@router.get("/{commune_id}", response_model=CommuneResponse)
def read_commune(commune_id: int, db: Session = Depends(get_db)) -> CommuneResponse:
    return get_commune(commune_id, db)

@router.put("/{commune_id}", response_model=CommuneResponse)
def update_commune(commune_id: int, commune: CommuneUpdate, db: Session = Depends(get_db)) -> CommuneResponse:
    return update_commune(commune, commune_id, db)

@router.delete("/{commune_id}", response_model=CommuneResponse)
def delete_commune(commune_id: int, db: Session = Depends(get_db)) -> dict:
    return delete_commune(commune_id, db)
