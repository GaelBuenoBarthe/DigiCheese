from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.stocks.poids import PoidsCreate, PoidsResponse
from app.infrastructure.api.stock.poids_controller import (
    get_all_poids as getallfromcontroller,
    get_poids as getfromcontroller,
    create_poids as createfromcontroller,
    update_poids as updatefromcontroller,
    delete_poids as deletefromcontroller,
)

router = APIRouter()

# Get all Poids entries
@router.get("/", response_model=list[PoidsResponse])
def route_get_all_poids(db: Session =  Depends (get_db),skip: int = 0, limit: int = 10 ):
    return getallfromcontroller(skip, limit, db)

# Get a Poids entry by ID
@router.get("/{id}", response_model=PoidsResponse)
def route_get_poids(id: int, db: Session =  Depends (get_db)):
    return getfromcontroller(id, db)

# Create a new Poids entry
@router.post("/", response_model=PoidsResponse)
def route_create_poids(poids: PoidsCreate, db: Session =  Depends (get_db)):
    return createfromcontroller(poids, db)

# Update an existing Poids entry
@router.put("/{id}", response_model=PoidsResponse)
def route_update_poids(id: int, poids_update: PoidsCreate, db: Session =  Depends (get_db)):
    return updatefromcontroller(id, poids_update, db)

# Delete a Poids entry
@router.delete("/{id}", response_model=PoidsResponse)
def route_delete_poids(id: int, db: Session =  Depends (get_db)):
    return deletefromcontroller(id, db)
