from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.client import Client
from app.schemas.client import ClientCreate, ClientUpdate, ClientResponse


def get_all_clients(skip: int, limit: int, db: Session):
    """
    Retrieves all clients with pagination.

    Raises a 500 Internal Server Error if an unexpected database error occurs.
    """
    try:
        return db.query(Client).offset(skip).limit(limit).all()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while retrieving clients: {str(e)}"
        )


def get_client(id: int, db: Session):
    """
    Retrieves a client by its ID.

    Raises a 404 Not Found exception if the client doesn't exist.
    Raises a 500 Internal Server Error if an unexpected database error occurs.
    """
    try:
        client = db.query(Client).filter(Client.id == id).first()
        if not client:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
        return client
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while retrieving client: {str(e)}"
        )


def create_client(client: ClientCreate, db: Session) -> ClientResponse:
    """
    Creates a new client.

    Raises a 400 Bad Request exception if a constraint violation or other database error occurs.
    """
    try:
        db_client = Client(**client.dict())
        db.add(db_client)
        db.commit()
        db.refresh(db_client)
        return db_client  # Make sure this returns the expected model for the route
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
    """
    Updates an existing client.

    Raises a 404 Not Found exception if the client doesn't exist.
    Raises a 400 Bad Request exception if a constraint violation or other database error occurs.
    """
    try:
        db_client = db.query(Client).filter(Client.id == id).first()
        if not db_client:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")

        for key, value in client_update.dict(exclude_unset=True).items():
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
    """
    Deletes a client by its ID.

    Raises a 404 Not Found exception if the client doesn't exist.
    Raises a 500 Internal Server Error if an unexpected database error occurs.
    """
    try:
        db_client = db.query(Client).filter(Client.id == id).first()
        if not db_client:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")

        db.delete(db_client)
        db.commit()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while deleting the client: {str(e)}"
        )