from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.infrastructure.api.commande.commandes_controller import (
    create_commande as create_commande_controller,
    delete_commande as delete_commande_controller,
    update_commande as update_commande_controller,
    get_commande as get_commande_controller,
    get_commandes as get_commandes_controller
)
from app.schemas.commandes.commande import Commande, CommandeCreate
from app.database import get_db

router = APIRouter()

@router.post("/commandes/", response_model=Commande)
def create_commande_route(commande: CommandeCreate, db: Session = Depends(get_db)):
    return create_commande_controller(db=db, commande=commande)

@router.get("/commandes/{id}", response_model=Commande)
def read_commande_route(id: int, db: Session = Depends(get_db)):
    return get_commande_controller(id, db)

@router.get("/commandes/", response_model=List[Commande])
def read_commandes_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_commandes_controller(db, skip=skip, limit=limit)

@router.put("/commandes/{id}", response_model=Commande)
def update_commande_route(id: int, commande: CommandeCreate, db: Session = Depends(get_db)):
    return update_commande_controller(db=db, id=id, commande=commande)

@router.delete("/commandes/{id}", response_model=Commande)
def delete_commande_route(id: int, db: Session = Depends(get_db)):
    return delete_commande_controller(db=db, id=id)
