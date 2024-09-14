import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.models.client.Departement import Departement
from app.schemas.Departement import DepartementCreate, DepartementUpdate
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
def create_test_departement(db_session: Session):
    test_departement = Departement(name="Test Departement")
    db_session.add(test_departement)
    db_session.commit()
    db_session.refresh(test_departement)
    return test_departement

def test_create_departement_success(db_session: Session):
    new_departement = {
        "name": "New Departement"
    }
    response = client.post("/departements/", json=new_departement)
    assert response.status_code == 201
    assert response.json()["name"] == "New Departement"

def test_create_departement_failure(db_session: Session):
    invalid_departement = {
        "name": ""  # Invalid name
    }
    response = client.post("/departements/", json=invalid_departement)
    assert response.status_code == 422

def test_get_departement_success(create_test_departement, db_session: Session):
    departement_id = create_test_departement.id
    response = client.get(f"/departements/{departement_id}")
    assert response.status_code == 200
    assert response.json()["id"] == departement_id

def test_get_departement_failure(db_session: Session):
    invalid_departement_id = 9999
    response = client.get(f"/departements/{invalid_departement_id}")
    assert response.status_code == 404

def test_update_departement_success(create_test_departement, db_session: Session):
    departement_id = create_test_departement.id
    updated_data = {
        "name": "Updated Departement"
    }
    response = client.put(f"/departements/{departement_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Departement"

def test_update_departement_failure(db_session: Session):
    invalid_departement_id = 9999
    updated_data = {
        "name": "Non-existent Departement"
    }
    response = client.put(f"/departements/{invalid_departement_id}", json=updated_data)
    assert response.status_code == 404

def test_delete_departement_success(create_test_departement, db_session: Session):
    departement_id = create_test_departement.id
    response = client.delete(f"/departements/{departement_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Departement deleted successfully"}

    response = client.get(f"/departements/{departement_id}")
    assert response.status_code == 404

def test_delete_departement_failure(db_session: Session):
    invalid_departement_id = 9999
    response = client.delete(f"/departements/{invalid_departement_id}")
    assert response.status_code == 404

def test_get_all_departements_success(create_test_departement, db_session: Session):
    response = client.get("/departements/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_all_departements_empty(db_session: Session):
    response = client.get("/departements/")
    assert response.status_code == 200
    assert len(response.json()) == 0
