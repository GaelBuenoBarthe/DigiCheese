from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.client.client import Client
from app.schemas.client.client import ClientCreate, ClientUpdate, ClientResponse

def get_all_clients(skip: int, limit: int, db: Session):
    try:
        clients = db.query(Client).offset(skip).limit(limit).all()
        return clients
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while retrieving clients: {str(e)}"
        )

def get_client(client_id: int, db: Session):
    try:
        client = db.query(Client).filter(Client.codcli == client_id).first()
        if not client:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client inexistant")
        return client
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while retrieving the client: {str(e)}"
        )

def create_client(client: ClientCreate, db: Session) -> ClientResponse:
    try:
        db_client = Client(**client.dict())
        db.add(db_client)
        db.commit()
        db.refresh(db_client)
        return db_client
    except IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"An error occurred while creating the client: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )

def update_client(id: int, client_update: ClientUpdate, db: Session):
    try:
        db_client = db.query(Client).filter(Client.codcli == id).first()
        if not db_client:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")

        for key, value in client_update.model_dump(exclude_unset=True).items():
            setattr(db_client, key, value)

        db.commit()
        db.refresh(db_client)
        return db_client
    except IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"An error occurred while updating the client: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )

def delete_client(id: int, db: Session):
    try:
        db_client = db.query(Client).filter(Client.codcli == id).first()
        if not db_client:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")

        db.delete(db_client)
        db.commit()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while deleting the client: {str(e)}"
        )