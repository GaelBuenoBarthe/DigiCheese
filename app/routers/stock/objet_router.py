from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal, get_db
from app.schemas.objet import ObjetCreate, ObjetUpdate, ObjetResponse
from app.infrastructure.api.stock.objets_controller import (
    get_all_objets as getallfromcontroller,
    get_objet as getfromcontroller,
    create_objet as createfromcontroller,
    update_objet as updatefromcontroller,
    delete_objet as deletefromcontroller,
)

router = APIRouter()

# Get all Objet entries
@router.get("/", response_model=list[ObjetResponse])
def route_get_all_objets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return getallfromcontroller(skip, limit, db)

# Get an Objet entry by ID
@router.get("/{id}", response_model=ObjetResponse)
def route_get_objet(id: int, db: Session = Depends(get_db)):
    return getfromcontroller(id, db)

# Create a new Objet entry
@router.post("/", response_model=ObjetResponse)
def route_create_objet(objet: ObjetCreate, db: Session = Depends(get_db)):
    return createfromcontroller(objet, db)

# Update an existing Objet entry
@router.put("/{id}", response_model=ObjetResponse)
def route_update_objet(id: int, objet_update: ObjetUpdate, db: Session = Depends(get_db)):
    return updatefromcontroller(id, objet_update, db)

# Delete an Objet entry
@router.delete("/{id}", response_model=ObjetResponse)
def route_delete_objet(id: int, db: Session = Depends(get_db)):
    return deletefromcontroller(id, db)
