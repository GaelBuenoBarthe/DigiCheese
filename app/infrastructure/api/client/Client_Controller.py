from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.client import Client
from app.schemas.Client import ClientCreate, ClientUpdate

def get_all_clients(skip: int, limit: int, db: Session):
    """
    Récupère tous les clients avec pagination.
    """
    return db.query(Client).offset(skip).limit(limit).all()

def get_client(id: int, db: Session):
    """
    Récupère un client par son ID.
    """
    client = db.query(Client).filter(Client.id == id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return client

def create_client(client: ClientCreate, db: Session):
    """
    Crée un nouveau client.
    """
    db_client = Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def update_client(id: int, client_update: ClientUpdate, db: Session):
    """
    Met à jour un client existant
    """
    db_client = db.query(Client).filter(Client.id == id).first()
    if not db_client:
        raise HTTPException(status_code=404, detail="Client non trouvé")

    for key, value in client_update.dict(exclude_unset=True).items():
        setattr(db_client, key, value)

    db.commit()
    db.refresh(db_client)
    return db_client

def delete_client(id: int, db: Session):
    """
    Supprime un client
    """
    db_client = db.query(Client).filter(Client.id == id).first()
    if not db_client:
        raise HTTPException(status_code=404, detail="Client non trouvé")

    db.delete(db_client)
    db.commit()
    return db_client