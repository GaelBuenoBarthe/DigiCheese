from sqlalchemy.orm import Session
from app.models.client import client as ClientModel
from app.schemas import client as schemas

def get_client(db: Session, client_id: int):
    return db.query(ClientModel).filter(ClientModel.id == client_id).first()

def get_clients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ClientModel).offset(skip).limit(limit).all()

def create_client(db: Session, client: schemas.ClientCreate):
    db_client = ClientModel
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def update_client(db: Session, client_id: int, client: schemas.ClientUpdate):
    db_client = db.query(ClientModel).filter(ClientModel.id == client_id).first()
    if db_client:
        for key, value in client.dict().items():
            setattr(db_client, key, value)
        db.commit()
        db.refresh(db_client)
    return db_client

def delete_client(db: Session, client_id: int):
    db_client = db.query(ClientModel).filter(ClientModel.id == client_id).first()
    if db_client:
        db.delete(db_client)
        db.commit()
    return db_client