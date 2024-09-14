from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.Poids import PoidsCreate, PoidsResponse
from app.infrastructure.api.stock.Poids_Controller import (
    get_all_poids,
    get_poids,
    create_poids,
    update_poids,
    delete_poids,
)

router = APIRouter()

# Get all Poids entries
@router.get("/", response_model=list[PoidsResponse])
def route_get_all_poids(db: Session =  Depends (get_db),skip: int = 0, limit: int = 10 ):
    return get_all_poids(skip, limit, db)

# Get a Poids entry by ID
@router.get("/{id}", response_model=PoidsResponse)
def route_get_poids(id: int, db: Session =  Depends (get_db)):
    return get_poids(id, db)

# Create a new Poids entry
@router.post("/", response_model=PoidsResponse)
def route_create_poids(poids: PoidsCreate, db: Session =  Depends (get_db)):
    return create_poids(poids, db)

# Update an existing Poids entry
@router.put("/{id}", response_model=PoidsResponse)
def route_update_poids(id: int, poids_update: PoidsCreate, db: Session =  Depends (get_db)):
    return update_poids(id, poids_update, db)

# Delete a Poids entry
@router.delete("/{id}", response_model=PoidsResponse)
def route_delete_poids(id: int, db: Session =  Depends (get_db)):
    return delete_poids(id, db)
