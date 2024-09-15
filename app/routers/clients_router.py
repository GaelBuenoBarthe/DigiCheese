from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.client import Client
from app.schemas.client import ClientCreate, ClientUpdate, ClientResponse
from app.infrastructure.api.client import (
    get_client, get_all_clients, delete_client, create_client, update_client
)

router = APIRouter()

@router.get("/", response_model=List[ClientResponse])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[ClientResponse]:
    """
    Récupère tous les clients avec pagination optionnelle.
    """
    clients = get_all_clients(skip, limit, db)
    return [ClientResponse.from_orm(client) for client in clients]

@router.post("/", response_model=ClientResponse, status_code=201)
def create_client(client: ClientCreate, db: Session = Depends(get_db)) -> ClientResponse:
    """
    Crée un nouveau client.
    """
    new_client = create_client(client, db)
    return ClientResponse.from_orm(new_client)

@router.get("/{client_id}", response_model=ClientResponse)
def read_client(client_id: int, db: Session = Depends(get_db)) -> ClientResponse:
    """
    Récupère un client par son ID.
    """
    client = get_client(client_id, db)
    return ClientResponse.from_orm(client)

@router.put("/{client_id}", response_model=ClientResponse)
def update_client(client_id: int, client: ClientUpdate, db: Session = Depends(get_db)) -> ClientResponse:
    """
    Met à jour un client existant.
    """
    updated_client = update_client(client, client_id, db)
    return ClientResponse.from_orm(updated_client)

@router.delete("/{client_id}", response_model=dict)
def delete_client(client_id: int, db: Session = Depends(get_db)) -> dict:
    """
    Supprime un client par son ID.
    """
    return delete_client(client_id, db)
