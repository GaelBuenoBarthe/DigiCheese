from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.client import Client
from app.schemas.client import ClientCreate, ClientUpdate
from app.infrastructure.api.client import (
    get_client, get_all_clients, delete_client, create_client, update_client
)

router = APIRouter()

@router.get("/", response_model=List[Client])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[Client]:
    """
    Récupère tous les clients avec pagination optionnelle.

    Args:
        skip: Nombre de clients à sauter (pour la pagination).
        limit: Nombre maximum de clients à retourner (pour la pagination).
        db: Session de base de données SQLAlchemy (injectée automatiquement par FastAPI).

    Returns:
        Une liste de clients.
    """
    return get_all_clients(skip, limit, db)

@router.post("/", response_model=Client, status_code=201)
def create_client(client: ClientCreate, db: Session = Depends(get_db)) -> Client:
    """
    Crée un nouveau client.

    Args:
        client: Données du nouveau client (validées par le schéma ClientCreate).
        db: Session de base de données SQLAlchemy.

    Returns:
        Le client créé.
    """
    return create_client(client, db)

@router.get("/{client_id}", response_model=Client)
def read_client(client_id: int, db: Session = Depends(get_db)) -> Client:
    """
    Récupère un client par son ID.

    Args:
        client_id: ID du client à récupérer.
        db: Session de base de données SQLAlchemy.

    Returns:
        Le client correspondant à l'ID donné.

    Raises:
        HTTPException: Si aucun client n'est trouvé avec l'ID donné (status_code 404).
    """
    db_client = get_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return db_client

@router.put("/{client_id}", response_model=Client)
def update_client(client_id: int, client: ClientUpdate, db: Session = Depends(get_db)) -> Client:
    """
    Met à jour un client existant.

    Args:
        client_id: ID du client à mettre à jour.
        client: Nouvelles données du client (validées par le schéma ClientUpdate).
        db: Session de base de données SQLAlchemy.

    Returns:
        Le client mis à jour.

    Raises:
        HTTPException: Si aucun client n'est trouvé avec l'ID donné (status_code 404).
    """
    db_client = update_client(db, client_id=client_id, client=client)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return db_client

@router.delete("/{client_id}", response_model=Client)
def delete_client(client_id: int, db: Session = Depends(get_db)) -> dict:
    """
    Supprime un client.

    Args:
        client_id: ID du client à supprimer.
        db: Session de base de données SQLAlchemy.

    Returns:
        Un dictionnaire avec un message de succès.

    Raises:
        HTTPException: Si aucun client n'est trouvé avec l'ID donné (status_code 404).
    """
    deleted_client = delete_client(db, client_id=client_id)
    if deleted_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"message": "Client deleted successfully"}