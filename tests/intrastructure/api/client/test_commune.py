import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from app.main import app
from app.models.client.commune import Commune
from app.schemas.commune import CommuneCreate, CommuneUpdate
from app.database import SessionLocal, Base

client = TestClient(app)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Use an in-memory database for testing
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
@pytest.fixture(scope="module")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture
def create_test_commune(db_session: Session):
    test_commune = Commune()
    test_commune.code_postal = "12345"
    test_commune.nom ="Test Commune"
    test_commune.departement = 1
    db_session.add(test_commune)
    db_session.commit()
    db_session.refresh(test_commune)
    return test_commune

def test_create_commune_success(db_session: Session):
    new_commune = {
        "code_postal": "67890",
        "nom": "New Commune",
        "departement_id": 2
    }
    response = client.post("/communes/", json=new_commune)
    assert response.status_code == 201
    assert response.json()["nom"] == "New Commune"
    assert response.json()["code_postal"] == "67890"
    assert response.json()["departement_id"] == 2

def test_create_commune_failure(db_session: Session):
    invalid_commune = {
        "nom": "",  # Invalid, missing code_postal and departement_id
    }
    response = client.post("/communes/", json=invalid_commune)
    assert response.status_code == 422

def test_get_commune_success(create_test_commune: Commune, db_session: Session):
    commune_id = create_test_commune.id
    response = client.get(f"/communes/{commune_id}")
    assert response.status_code == 200
    assert response.json()["id"] == commune_id
    assert response.json()["nom"] == "Test Commune"

def test_get_commune_failure(db_session: Session):
    invalid_commune_id = 9999
    response = client.get(f"/communes/{invalid_commune_id}")
    assert response.status_code == 404

def test_update_commune_success(create_test_commune: Commune, db_session: Session):
    commune_id = create_test_commune.id
    updated_data = {
        "code_postal": "54321",
        "nom": "Updated Commune",
        "departement_id": 3
    }
    response = client.put(f"/communes/{commune_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["code_postal"] == "54321"
    assert response.json()["nom"] == "Updated Commune"
    assert response.json()["departement_id"] == 3

def test_update_commune_failure(db_session: Session):
    invalid_commune_id = 9999
    updated_data = {
        "code_postal": "00000",
        "nom": "Non-existent Commune",
        "departement_id": 999
    }
    response = client.put(f"/communes/{invalid_commune_id}", json=updated_data)
    assert response.status_code == 404

def test_delete_commune_success(create_test_commune: Commune, db_session: Session):
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

def test_get_all_communes_success(create_test_commune: Commune, db_session: Session):
    response = client.get("/communes/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert any(commune["nom"] == "Test Commune" for commune in data)

def test_get_all_communes_empty(db_session: Session):
    response = client.get("/communes/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 0
