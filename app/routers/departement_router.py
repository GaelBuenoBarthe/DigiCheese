from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.departement import DepartementCreate, DepartementUpdate, DepartementResponse
from app.infrastructure.api.client.departement_controller import (
    get_departement, get_all_departements, delete_departement, create_departement, update_departement
)

router = APIRouter()


@router.get("/", response_model=List[DepartementResponse])
def read_departements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[DepartementResponse]:
    """
    Récupère tous les départements avec pagination optionnelle.

    Args:
        skip: Nombre de départements à sauter (pour la pagination).
        limit: Nombre maximum de départements à retourner (pour la pagination).
        db: Session de base de données SQLAlchemy (injectée automatiquement par FastAPI).

    Returns:
        Une liste de départements.
    """
    departements = get_all_departements(skip, limit, db)
    return departements


@router.post("/", response_model=DepartementResponse, status_code=201)
def create_departement(departement: DepartementCreate, db: Session = Depends(get_db)) -> DepartementResponse:
    """
    Crée un nouveau département.

    Args:
        departement: Schéma pour la création d'un département.
        db: Session de base de données SQLAlchemy (injectée automatiquement par FastAPI).

    Returns:
        Le département créé.
    """
    return create_departement(departement, db)


@router.get("/{departement_id}", response_model=DepartementResponse)
def read_departement(departement_id: int, db: Session = Depends(get_db)) -> DepartementResponse:
    """
    Récupère un département par son ID.

    Args:
        departement_id: ID du département à récupérer.
        db: Session de base de données SQLAlchemy (injectée automatiquement par FastAPI).

    Returns:
        Le département correspondant à l'ID fourni.
    """
    return get_departement(departement_id, db)


@router.put("/{departement_id}", response_model=DepartementResponse)
def update_departement(departement_id: int, departement: DepartementUpdate,
                       db: Session = Depends(get_db)) -> DepartementResponse:
    """
    Met à jour un département existant.

    Args:
        departement_id: ID du département à mettre à jour.
        departement: Schéma pour la mise à jour du département.
        db: Session de base de données SQLAlchemy (injectée automatiquement par FastAPI).

    Returns:
        Le département mis à jour.
    """
    return update_departement(departement_id, departement, db)


@router.delete("/{departement_id}", response_model=DepartementResponse)
def delete_departement(departement_id: int, db: Session = Depends(get_db)) -> DepartementResponse:
    """
    Supprime un département.

    Args:
        departement_id: ID du département à supprimer.
        db: Session de base de données SQLAlchemy (injectée automatiquement par FastAPI).

    Returns:
        Le département supprimé.
    """
    return delete_departement(departement_id, db)
