from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.stock.objet_cond import ObjetCondCreate, ObjetCondResponse
from app.infrastructure.api.stock.objet_conds_controller import (
    get_all_objet_cond as getallfromcontroller,
    get_objet_cond as getfromcontroller,
    create_objet_cond as createfromcontroller,
    update_objet_cond as updatefromcontroller,
)

router = APIRouter()

# Get all ObjetCond entries
@router.get("/", response_model=list[ObjetCondResponse])
def route_get_all_objet_cond(db: Session=  Depends (get_db), skip: int = 0, limit: int = 10 ):
    return getallfromcontroller(skip, limit, db)

# Get an ObjetCond by ID
@router.get("/{idrelcond}", response_model=ObjetCondResponse)
def route_get_objet_cond(idrelcond: int, db: Session =  Depends (get_db)):
    return getfromcontroller(idrelcond, db)

# Create a new ObjetCond
@router.post("/", response_model=ObjetCondResponse)
def route_create_objet_cond(objet_cond: ObjetCondCreate, db: Session =  Depends (get_db)):
    return createfromcontroller(objet_cond, db)

# Update an existing ObjetCond
@router.put("/{idrelcond}", response_model=ObjetCondResponse)
def route_update_objet_cond(idrelcond: int, objet_cond_update: ObjetCondCreate, db: Session =  Depends (get_db)):
    return updatefromcontroller(idrelcond, objet_cond_update, db)

# Delete an ObjetCond
@router.delete("/{idrelcond}", response_model=ObjetCondResponse)
def route_delete_objet_cond(idrelcond: int, db: Session =  Depends (get_db)):
    return updatefromcontroller(idrelcond, db)
