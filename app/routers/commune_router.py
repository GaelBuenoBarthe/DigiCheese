from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.commune import CommuneCreate, CommuneUpdate, CommuneResponse
from app.infrastructure.api.client.commune_controller import (
    get_commune as get_commune_controller,
    get_all_communes as get_all_communes_controller,
    delete_commune as delete_commune_controller,
    create_commune as create_commune_controller,
    update_commune as update_commune_controller
)

router = APIRouter()

@router.get("/", response_model=List[CommuneResponse])
def read_communes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[CommuneResponse]:
    return get_all_communes_controller(skip, limit, db)

@router.post("/", response_model=CommuneResponse, status_code=201)
def create_commune_route(commune: CommuneCreate, db: Session = Depends(get_db)) -> CommuneResponse:
    return create_commune_controller(commune, db)

@router.get("/{commune_id}", response_model=CommuneResponse)
def read_commune_route(commune_id: int, db: Session = Depends(get_db)) -> CommuneResponse:
    return get_commune_controller(commune_id, db)

@router.put("/{commune_id}", response_model=CommuneResponse)
def update_commune_route(commune_id: int, commune: CommuneUpdate, db: Session = Depends(get_db)) -> CommuneResponse:
    return update_commune_controller(commune, commune_id, db)

@router.delete("/{commune_id}", response_model=CommuneResponse)
def delete_commune_route(commune_id: int, db: Session = Depends(get_db)) -> dict:
    return delete_commune_controller(commune_id, db)
