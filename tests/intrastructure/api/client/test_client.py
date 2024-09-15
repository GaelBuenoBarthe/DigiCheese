import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from app.main import app
from app.models.client import Client
from app.database import SessionLocal, Base

client = TestClient(app)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Use an in-memory database for testing
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture
def create_test_client(db_session: Session):
    """
    Fixture to create a test client using the custom constructor
    """
    test_client = Client(
        genre="M",
        nom="Test Client",
        prenom="John",
        adresse1="123 Test St",
        adresse2=None,
        adresse3=None,
        ville_id=1,
        telephone="0123456789",
        email="test@example.com",
        portable="0987654321",
        newsletter=True
    )

    db_session.add(test_client)
    db_session.commit()
    db_session.refresh(test_client)
    return test_client

def test_create_client_success(db_session: Session):
    """
    Test to create a client successfully and verify the database insertion
    """
    new_client_data = {
        "genre": "M",
        "nom": "New Client",
        "prenom": "Jane",
        "adresse1": "456 New St",
        "adresse2": None,
        "adresse3": None,
        "ville_id": 1,
        "telephone": "0987654321",
        "email": "new@example.com",
        "portable": "1234567890",
        "newsletter": False
    }
    # Send POST request to create a new client via API
    response = client.post("/clients/", json=new_client_data)
    assert response.status_code == 201

    created_client = response.json()
    assert created_client["nom"] == "New Client"
    assert created_client["email"] == "new@example.com"
    assert created_client["adresse1"] == "456 New St"
    assert created_client["telephone"] == "0987654321"

    # Query the database to ensure the client was inserted
    db_client = db_session.query(Client).filter_by(email="new@example.com").first()
    assert db_client is not None
    assert db_client.nom == "New Client"
    assert db_client.email == "new@example.com"
    assert db_client.adresse1 == "456 New St"
    assert db_client.telephone == "0987654321"

def test_create_client_failure(db_session: Session):
    """
    Test to create a client with invalid data (missing required fields)
    """
    invalid_client_data = {
        "email": "invalid@example.com"  # Missing other required fields
    }
    response = client.post("/clients/", json=invalid_client_data)
    assert response.status_code == 422

def test_get_client_success(create_test_client: Client, db_session: Session):
    """
    Test to retrieve a client by codcli successfully
    """
    client_id = create_test_client.codcli  # Use codcli as primary key
    response = client.get(f"/clients/{client_id}")
    assert response.status_code == 200
    client_data = response.json()
    assert client_data["codcli"] == client_id
    assert client_data["nom"] == "Test Client"
    assert client_data["email"] == "test@example.com"
    assert client_data["adresse1"] == "123 Test St"
    assert client_data["telephone"] == "0123456789"

def test_get_client_failure(db_session: Session):
    """
    Test to retrieve a non-existent client by codcli
    """
    invalid_client_id = 9999
    response = client.get(f"/clients/{invalid_client_id}")
    assert response.status_code == 404

def test_update_client_success(create_test_client: Client, db_session: Session):
    """
    Test to update an existing client successfully
    """
    client_id = create_test_client.codcli  # Use codcli as primary key
    updated_data = {
        "genre": "F",
        "nom": "Updated Client",
        "prenom": "Jane",
        "adresse1": "789 Updated St",
        "adresse2": None,
        "adresse3": None,
        "ville_id": 1,
        "telephone": "1234567890",
        "email": "updated@example.com",
        "portable": "9876543210",
        "newsletter": True
    }
    response = client.put(f"/clients/{client_id}", json=updated_data)
    assert response.status_code == 200
    updated_client = response.json()
    assert updated_client["codcli"] == client_id
    assert updated_client["nom"] == "Updated Client"
    assert updated_client["email"] == "updated@example.com"
    assert updated_client["adresse1"] == "789 Updated St"
    assert updated_client["telephone"] == "1234567890"

def test_update_client_failure(db_session: Session):
    """
    Test to update a non-existent client
    """
    invalid_client_id = 9999
    updated_data = {
        "genre": "M",
        "nom": "Non-existent Client",
        "prenom": "Non",
        "adresse1": "000 No St",
        "adresse2": None,
        "adresse3": None,
        "ville_id": 1,
        "telephone": "0000000000",
        "email": "nonexistent@example.com",
        "portable": "0000000000",
        "newsletter": False
    }
    response = client.put(f"/clients/{invalid_client_id}", json=updated_data)
    assert response.status_code == 404

def test_delete_client_success(create_test_client: Client, db_session: Session):
    """
    Test to delete an existing client successfully
    """
    client_id = create_test_client.codcli  # Use codcli as primary key
    response = client.delete(f"/clients/{client_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Client deleted successfully"}

    # Confirm that the client has been deleted
    response = client.get(f"/clients/{client_id}")
    assert response.status_code == 404

def test_delete_client_failure(db_session: Session):
    """
    Test to delete a non-existent client
    """
    invalid_client_id = 9999
    response = client.delete(f"/clients/{invalid_client_id}")
    assert response.status_code == 404

def test_get_all_clients_success(create_test_client: Client, db_session: Session):
    """
    Test to retrieve all clients with pagination
    """
    response = client.get("/clients/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert any(client["nom"] == "Test Client" for client in data)

def test_get_all_clients_empty(db_session: Session):
    """
    Test to retrieve all clients when no clients exist
    """
    # Ensure no clients exist in the database
    db_session.query(Client).delete()
    db_session.commit()

    response = client.get("/clients/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 0
