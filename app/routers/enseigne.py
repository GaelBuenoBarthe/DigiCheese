from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.client.enseigne import Enseigne
from app.schemas.enseigne import EnseigneCreate, EnseigneUpdate
from app.infrastructure.api.client import enseigne_controller as controller

router = APIRouter()

@router.get("/", response_model=List[Enseigne])
def route_get_all_enseignes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Récupère toutes les enseignes avec pagination optionnelle.
    """
    return controller.get_all_enseignes(skip, limit, db)

@router.post("/", response_model=Enseigne, status_code=status.HTTP_201_CREATED)
def route_create_enseigne(enseigne: EnseigneCreate, db: Session = Depends(get_db)):
    """
    Crée une nouvelle enseigne
    """
    return controller.create_enseigne(enseigne, db)

@router.get("/{enseigne_id}", response_model=Enseigne)
def route_get_enseigne(enseigne_id: int, db: Session = Depends(get_db)):

   return controller.get_enseigne(enseigne_id, db)

@router.put("/{enseigne_id}", response_model=Enseigne)
def route_update_enseigne(enseigne_id: int, enseigne: EnseigneUpdate, db: Session = Depends(get_db)):

   return controller.update_enseigne(enseigne_id, enseigne, db)

@router.delete("/{enseigne_id}")
def route_delete_enseigne(enseigne_id: int, db: Session = Depends(get_db)):
    """
    Supprime une enseigne
    """
    return controller.delete_enseigne(enseigne_id, db)
