from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.client.client import ClientCreate, ClientUpdate, ClientResponse
from app.infrastructure.api.client.client_controller import (
    get_all_clients,
    delete_client as delete_client_controller,
    create_client as create_client_controller,
    update_client as update_client_controller,
    get_client
)

router = APIRouter()

@router.get("/", response_model=List[ClientResponse])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_clients(skip, limit, db)

@router.get("/{client_id}", response_model=ClientResponse)
def read_client(client_id: int, db: Session = Depends(get_db)):
    client = get_client(client_id, db)
    if not client:
        raise HTTPException(status_code=404, detail="Client introuvable")
    return client

@router.post("/", response_model=ClientResponse, status_code=201)
def create_client_route(client: ClientCreate, db: Session = Depends(get_db)) -> ClientResponse:
    new_client = create_client_controller(client, db)
    return ClientResponse.model_validate(new_client)

@router.put("/{client_id}", response_model=ClientResponse)
def update_client_route(client_id: int, client: ClientUpdate, db: Session = Depends(get_db)) -> ClientResponse:
    updated_client = update_client_controller(client_id, client, db)
    return ClientResponse.model_validate(updated_client)

@router.delete("/{client_id}", response_model=dict)
def delete_client_route(client_id: int, db: Session = Depends(get_db)) -> dict:
    return delete_client_controller(client_id, db)