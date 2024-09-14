import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.models.client.commune import Commune
from app.schemas.commune import CommuneCreate, CommuneUpdate
from app.database import SessionLocal

client = TestClient(app)

@pytest.fixture(scope="module")
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def create_test_commune(db_session: Session):
    test_commune = Commune(
        code_postal="12345",
        nom="Test Commune",
        departement_id=1
    )
    db_session.add(test_commune)
    db_session.commit()
    db_session.refresh(test_commune)
    return test_commune

def test_create_commune_success(db_session: Session):
    new_commune = {
        "code_postal": "67890",
        "nom": "New Commune",
        "departement_id": 1
    }
    response = client.post("/communes/", json=new_commune)
    assert response.status_code == 201
    assert response.json()["nom"] == "New Commune"

def test_create_commune_failure(db_session: Session):
    invalid_commune = {
        "code_postal": "67890",
        "nom": "",  # Invalid name
        "departement_id": 1
    }
    response = client.post("/communes/", json=invalid_commune)
    assert response.status_code == 422

def test_get_commune_success(create_test_commune, db_session: Session):
    commune_id = create_test_commune.id
    response = client.get(f"/communes/{commune_id}")
    assert response.status_code == 200
    assert response.json()["id"] == commune_id

def test_get_commune_failure(db_session: Session):
    invalid_commune_id = 9999
    response = client.get(f"/communes/{invalid_commune_id}")
    assert response.status_code == 404

def test_update_commune_success(create_test_commune, db_session: Session):
    commune_id = create_test_commune.id
    updated_data = {
        "nom": "Updated Commune"
    }
    response = client.put(f"/communes/{commune_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["nom"] == "Updated Commune"

def test_update_commune_failure(db_session: Session):
    invalid_commune_id = 9999
    updated_data = {
        "nom": "Non-existent Commune"
    }
    response = client.put(f"/communes/{invalid_commune_id}", json=updated_data)
    assert response.status_code == 404

def test_delete_commune_success(create_test_commune, db_session: Session):
    commune_id = create_test_commune.id
    response = client.delete(f"/communes/{commune_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Commune deleted successfully"}

    response = client.get(f"/communes/{commune_id}")
    assert response.status_code == 404

def test_delete_commune_failure(db_session: Session):
    invalid_commune_id = 9999
    response = client.delete(f"/communes/{invalid_commune_id}")
    assert response.status_code == 404

def test_get_all_communes_success(create_test_commune, db_session: Session):
    response = client.get("/communes/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_all_communes_empty(db_session: Session):
    response = client.get("/communes/")
    assert response.status_code == 200
    assert len(response.json()) == 0
