from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.client.departement import Departement
from app.schemas.departement import DepartementCreate, DepartementUpdate
from app.infrastructure.api.client import departement_controller as controller

router = APIRouter()

@router.get("/", response_model=List[Departement])
def route_get_all_departements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Récupère tous les départements avec pagination optionnelle.
    """
    return controller.route_get_all_departements(db, skip, limit)

@router.post("/", response_model=Departement, status_code=status.HTTP_201_CREATED)
def route_create_departement(departement: DepartementCreate, db: Session = Depends(get_db)):
    """
    Crée un nouveau département
    """
    return controller.route_create_departement(departement, db)

@router.get("/{departement_id}", response_model=Departement)
def route_get_departement(departement_id: int, db: Session = Depends(get_db)):
    """
    Récupère un département par son ID
    """
    return controller.route_get_departement(departement_id, db)

@router.put("/{departement_id}", response_model=Departement)
def route_update_departement(departement_id: int, departement: DepartementUpdate, db: Session = Depends(get_db)):
    """
    Met à jour un département existant
    """
    return controller.route_update_departement(departement_id, departement, db)

@router.delete("/{departement_id}")
def route_delete_departement(departement_id: int, db: Session = Depends(get_db)):
    """
    Supprime un département
    """
    return controller.route_delete_departement(departement_id, db)