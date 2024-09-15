from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.vignette import VignetteCreate, VignetteResponse
from app.infrastructure.api.stock.vignettes_controller import (
    get_all_vignettes,
    get_vignette,
    create_vignette,
    update_vignette,
    delete_vignette,
)

router = APIRouter()

# Get all Vignette entries
@router.get("/", response_model=list[VignetteResponse])
def route_get_all_vignettes(db: Session = Depends(get_db), skip: int = 0, limit: int = 10 ):
    return get_all_vignettes(skip, limit, db)

# Get a Vignette entry by ID
@router.get("/{id}", response_model=VignetteResponse)
def route_get_vignette(id: int, db: Session = Depends(get_db)):
    return get_vignette(id, db)

# Create a new Vignette entry
@router.post("/", response_model=VignetteResponse)
def route_create_vignette(vignette: VignetteCreate, db: Session = Depends(get_db)):
    return create_vignette(vignette, db)

# Update an existing Vignette entry
@router.put("/{id}", response_model=VignetteResponse)
def route_update_vignette(id: int, vignette_update: VignetteCreate, db: Session = Depends(get_db)):
    return update_vignette(id, vignette_update, db)

# Delete a Vignette entry
@router.delete("/{id}", response_model=VignetteResponse)
def route_delete_vignette(id: int, db: Session = Depends(get_db)):
    return delete_vignette(id, db)
