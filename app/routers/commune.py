from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.client.commune import Commune
from app.schemas.commune import CommuneCreate, CommuneUpdate
from app.infrastructure.api.client import commune_controller as controller

router = APIRouter()

@router.get("/", response_model=List[Commune])
def route_get_all_communes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Récupère toutes les communes avec pagination optionnelle.
    """
    return controller.get_all_communes(skip, limit, db)

@router.post("/", response_model=Commune, status_code=status.HTTP_201_CREATED)
def route_create_commune(commune: CommuneCreate, db: Session = Depends(get_db)):
    """
    Crée une nouvelle commune.
    """
    return controller.create_commune(commune, db)

@router.get("/{commune_id}", response_model=Commune)
def route_get_commune(commune_id: int, db: Session = Depends(get_db)):
    """
    Récupère une commune par son ID.
    """
    db_commune = controller.get_commune(commune_id, db)
    if db_commune is None:
        raise HTTPException(status_code=404, detail="Commune non trouvée")
    return db_commune

@router.put("/{commune_id}", response_model=Commune)
def route_update_commune(commune_id: int, commune: CommuneUpdate, db: Session = Depends(get_db)):
    """
    Met à jour une commune existante.
    """
    db_commune = controller.update_commune(commune_id, commune, db)
    if db_commune is None:
        raise HTTPException(status_code=404, detail="Commune non trouvée")
    return db_commune

@router.delete("/{commune_id}")
def route_delete_commune(commune_id: int, db: Session = Depends(get_db)):
    """
    Supprime une commune.
    """
    controller.delete_commune(commune_id, db)
    return {"message": "Commune supprimée avec succès"}