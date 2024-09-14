from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, get_db
from app.schemas.detail_objet import DetailObjetCreate, DetailObjetResponse
from app.infrastructure.api.commande.detail_objet_controller import (
    get_all_detail_objets,
    get_detail_objet,
    create_detail_objet,
    update_detail_objet,
    delete_detail_objet,
)



router = APIRouter()

# Get all DetailObjet entries
@router.get("/", response_model=list[DetailObjetResponse])
def route_get_all_detail_objets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_all_detail_objets(skip, limit, db)

# Get a DetailObjet entry by ID
@router.get("/{id}", response_model=DetailObjetResponse)
def route_get_detail_objet(id: int, db: Session = Depends(get_db)):
    return get_detail_objet(id, db)

# Create a new DetailObjet entry
@router.post("/", response_model=DetailObjetResponse)
def route_create_detail_objet(detail_objet: DetailObjetCreate, db: Session = Depends(get_db)):
    return create_detail_objet(detail_objet, db)

# Update an existing DetailObjet entry
@router.put("/{id}", response_model=DetailObjetResponse)
def route_update_detail_objet(id: int, detail_objet_update: DetailObjetCreate, db: Session = Depends(get_db)):
    return update_detail_objet(id, detail_objet_update, db)

# Delete a DetailObjet entry
@router.delete("/{id}", response_model=DetailObjetResponse)
def route_delete_detail_objet(id: int, db: Session = Depends(get_db)):
    return delete_detail_objet(id, db)
