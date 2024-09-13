from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.poids import PoidsCreate, PoidsResponse
from app.infrastructure.api.stock.poids import (
    get_all_poids,
    get_poids,
    create_poids,
    update_poids,
    delete_poids,
)

router = APIRouter()

# Get all Poids entries
@router.get("/", response_model=list[PoidsResponse])
def route_get_all_poids(db: Session,skip: int = 0, limit: int = 10 ):
    return get_all_poids(skip, limit, db)

# Get a Poids entry by ID
@router.get("/{id}", response_model=PoidsResponse)
def route_get_poids(id: int, db: Session):
    return get_poids(id, db)

# Create a new Poids entry
@router.post("/", response_model=PoidsResponse)
def route_create_poids(poids: PoidsCreate, db: Session):
    return create_poids(poids, db)

# Update an existing Poids entry
@router.put("/{id}", response_model=PoidsResponse)
def route_update_poids(id: int, poids_update: PoidsCreate, db: Session):
    return update_poids(id, poids_update, db)

# Delete a Poids entry
@router.delete("/{id}", response_model=PoidsResponse)
def route_delete_poids(id: int, db: Session):
    return delete_poids(id, db)
