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

    return create_client(client, db)

@router.get("/{client_id}", response_model=Client)
def read_client(client_id: int, db: Session = Depends(get_db)) -> Client:

   return get_client(client_id, db)

@router.put("/{client_id}", response_model=Client)
def update_client(client_id: int, client: ClientUpdate, db: Session = Depends(get_db)) -> Client:

    return update_client(client, client_id, db)

@router.delete("/{client_id}", response_model=Client)
def delete_client(client_id: int, db: Session = Depends(get_db)) -> dict:

    return delete_client(client_id, db)