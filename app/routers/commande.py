from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud
from app.schemas.commande import Commande, CommandeCreate
from app.database import SessionLocal

router = APIRouter()

#Creation d'une fonction pour obtenir la session de la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Définition des routes "post" pour les commandes
@router.post("/commandes/", response_model=Commande)
def create_commande(commande: CommandeCreate, db: Session = Depends(get_db)):
    return crud.create_commande(db=db, commande=commande)

#Définition des routes "get" pour les id de commandes
@router.get("/commandes/{id}", response_model=Commande)
def read_commande(id: int, db: Session = Depends(get_db)):
    db_commande = crud.get_commande(db, id=id)
    if db_commande is None:
        raise HTTPException(status_code=404, detail="Commande non trouvée")
    return db_commande

#Définition des routes "get" pour les commandes
@router.get("/commandes/", response_model=List[Commande])
def read_commandes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_commandes(db, skip=skip, limit=limit)

#Définition des routes "put" pour les id de commandes
@router.put("/commandes/{id}", response_model=Commande)
def update_commande(id: int, commande: CommandeCreate, db: Session = Depends(get_db)):
    return crud.update_commande(db=db, id=id, commande=commande)

#Définition des routes "delete" pour les id de commandes
@router.delete("/commandes/{id}", response_model=Commande)
def delete_commande(id: int, db: Session = Depends(get_db)):
    return crud.delete_commande(db=db, id=id)