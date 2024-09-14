import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.models.client import Client
from app.schemas.client import ClientCreate, ClientUpdate
from app.database import SessionLocal, engine

client = TestClient(app)

@pytest.fixture(scope="module")
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def create_test_client(db_session: Session):
    test_client = Client(name="Test Client", email="testclient@example.com")
    db_session.add(test_client)
    db_session.commit()
    db_session.refresh(test_client)
    return test_client

def test_create_client_success(db_session: Session):
    new_client = {
        "name": "New Client",
        "email": "newclient@example.com"
    }
    response = client.post("/clients/", json=new_client)
    assert response.status_code == 201
    assert response.json()["name"] == "New Client"

def test_create_client_failure(db_session: Session):
    invalid_client = {
        "name": "",  # Invalid name
        "email": "invalidclient@example.com"
    }
    response = client.post("/clients/", json=invalid_client)
    assert response.status_code == 422

def test_get_client_success(create_test_client, db_session: Session):
    client_id = create_test_client.id
    response = client.get(f"/clients/{client_id}")
    assert response.status_code == 200
    assert response.json()["id"] == client_id

def test_get_client_failure(db_session: Session):
    invalid_client_id = 9999
    response = client.get(f"/clients/{invalid_client_id}")
    assert response.status_code == 404

def test_update_client_success(create_test_client, db_session: Session):
    client_id = create_test_client.id
    updated_data = {
        "name": "Updated Client",
        "email": "updatedclient@example.com"
    }
    response = client.put(f"/clients/{client_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Client"

def test_update_client_failure(db_session: Session):
    invalid_client_id = 9999
    updated_data = {
        "name": "Non-existent Client",
        "email": "nonexistentclient@example.com"
    }
    response = client.put(f"/clients/{invalid_client_id}", json=updated_data)
    assert response.status_code == 404

def test_delete_client_success(create_test_client, db_session: Session):
    client_id = create_test_client.id
    response = client.delete(f"/clients/{client_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Client deleted successfully"}

    response = client.get(f"/clients/{client_id}")
    assert response.status_code == 404

def test_delete_client_failure(db_session: Session):
    invalid_client_id = 9999
    response = client.delete(f"/clients/{invalid_client_id}")
    assert response.status_code == 404

def test_get_all_clients_success(create_test_client, db_session: Session):
    response = client.get("/clients/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_all_clients_empty(db_session: Session):
    response = client.get("/clients/")
    assert response.status_code == 200
    assert len(response.json()) == 0
