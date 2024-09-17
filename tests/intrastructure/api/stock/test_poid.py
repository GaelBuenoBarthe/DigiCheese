import pytest
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

from app.database import SessionLocal
from app.main import app
from app.models.stock.poids import Poids

client = TestClient(app)

@pytest.fixture(scope="module")
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def setup_poids(db_session: Session):
    poids = Poids(id=1, weight=10.0)
    db_session.add(poids)
    db_session.commit()
    db_session.refresh(poids)
    return poids

def test_get_all_poids(db_session: Session):
    response = client.get("/poids/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_poids_success(db_session: Session, setup_poids: Poids):
    response = client.get(f"/poids/{setup_poids.id}")
    assert response.status_code == 200
    assert response.json()["weight"] == 10.0

def test_get_poids_failure(db_session: Session):
    response = client.get("/poids/999")  # Non-existent ID
    assert response.status_code == 404

def test_create_poids_success(db_session: Session):
    poids_data = {"weight": 20.0}
    response = client.post("/poids/", json=poids_data)
    assert response.status_code == 200
    assert response.json()["weight"] == 20.0

def test_create_poids_failure(db_session: Session):
    # Example of failure: sending incomplete data
    poids_data = {}  # Required fields missing
    response = client.post("/poids/", json=poids_data)
    assert response.status_code == 422  # Unprocessable Entity

def test_update_poids_success(db_session: Session, setup_poids: Poids):
    update_data = {"weight": 15.0}
    response = client.put(f"/poids/{setup_poids.id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["weight"] == 15.0

def test_update_poids_failure(db_session: Session):
    update_data = {"weight": 15.0}
    response = client.put("/poids/999", json=update_data)  # Non-existent ID
    assert response.status_code == 404

def test_delete_poids_success(db_session: Session, setup_poids: Poids):
    response = client.delete(f"/poids/{setup_poids.id}")
    assert response.status_code == 200
    assert response.json()["id"] == setup_poids.id

def test_delete_poids_failure(db_session: Session):
    response = client.delete("/poids/999")  # Non-existent ID
    assert response.status_code == 404
