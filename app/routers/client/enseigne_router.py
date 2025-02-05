from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db

from app.schemas.client.enseigne import EnseigneCreate, EnseigneUpdate, EnseigneResponse
from app.infrastructure.api.client.enseigne_controller import (
    get_enseigne as getfromcontroller, get_all_enseignes as getallfromcontorller, delete_enseigne as deletefromcontroller,
    create_enseigne as createfromcontroller, update_enseigne as updatefromcontroller
)

router = APIRouter()


@router.get("/", response_model=List[EnseigneResponse])
def read_enseignes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[EnseigneResponse]:
    """
    Récupère toutes les enseignes avec pagination optionnelle.

    Args:
        skip: Nombre d'enseignes à sauter (pour la pagination).
        limit: Nombre maximum d'enseignes à retourner (pour la pagination).
        db: Session de base de données SQLAlchemy (injectée automatiquement par FastAPI).

    Returns:
        Une liste d'enseignes.
    """
    enseignes = getallfromcontorller(skip, limit, db)
    return enseignes


@router.post("/", response_model=EnseigneResponse, status_code=201)
def create_enseigne(enseigne: EnseigneCreate, db: Session = Depends(get_db)) -> EnseigneResponse:
    """
    Crée une nouvelle enseigne.

    Args:
        enseigne: Schéma pour la création d'une enseigne.
        db: Session de base de données SQLAlchemy (injectée automatiquement par FastAPI).

    Returns:
        L'enseigne créée.
    """
    return createfromcontroller(enseigne, db)


@router.get("/{enseigne_id}", response_model=EnseigneResponse)
def read_enseigne(enseigne_id: int, db: Session = Depends(get_db)) -> EnseigneResponse:
    """
    Récupère une enseigne par son ID.

    Args:
        enseigne_id: ID de l'enseigne à récupérer.
        db: Session de base de données SQLAlchemy (injectée automatiquement par FastAPI).

    Returns:
        L'enseigne correspondant à l'ID fourni.
    """
    return getfromcontroller(enseigne_id, db)


@router.put("/{enseigne_id}", response_model=EnseigneResponse)
def update_enseigne(enseigne_id: int, enseigne: EnseigneUpdate, db: Session = Depends(get_db)) -> EnseigneResponse:
    """
    Met à jour une enseigne existante.

    Args:
        enseigne_id: ID de l'enseigne à mettre à jour.
        enseigne: Schéma pour la mise à jour de l'enseigne.
        db: Session de base de données SQLAlchemy (injectée automatiquement par FastAPI).

    Returns:
        L'enseigne mise à jour.
    """
    return updatefromcontroller (enseigne_id, enseigne, db)


@router.delete("/{enseigne_id}", response_model=EnseigneResponse)
def delete_enseigne(enseigne_id: int, db: Session = Depends(get_db)) -> EnseigneResponse:
    """
    Supprime une enseigne.

    Args:
        enseigne_id: ID de l'enseigne à supprimer.
        db: Session de base de données SQLAlchemy (injectée automatiquement par FastAPI).

    Returns:
        L'enseigne supprimée.
    """
    return deletefromcontroller(enseigne_id, db)
