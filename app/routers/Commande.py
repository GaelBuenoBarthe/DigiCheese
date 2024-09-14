from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.infrastructure.api.commande.Commandes_Controller import  create_commande,delete_commande,update_commande,get_commande,get_commandes
from app.schemas.Commande import Commande, CommandeCreate
from app.database import SessionLocal, get_db

router = APIRouter()



@router.post("/commandes/", response_model=Commande)
def create_commande(commande: CommandeCreate, db: Session = Depends(get_db)):
    return create_commande(db=db, commande=commande)

@router.get("/commandes/{id}", response_model=Commande)
def read_commande(id: int, db: Session = Depends(get_db)):
    return get_commande(id, db)

@router.get("/commandes/", response_model=List[Commande])
def read_commandes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_commandes(db, skip=skip, limit=limit)

@router.put("/commandes/{id}", response_model=Commande)
def update_commande(id: int, commande: CommandeCreate, db: Session = Depends(get_db)):
    return update_commande(db=db, id=id, commande=commande)

@router.delete("/commandes/{id}", response_model=Commande)
def delete_commande(id: int, db: Session = Depends(get_db)):
    return delete_commande(db=db, id=id)