import pytest
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

from app.database import SessionLocal
from app.main import app
from app.models.stock.objet import Objet
from app.schemas.objet import ObjetCreate, ObjetUpdate

client = TestClient(app)

@pytest.fixture(scope="module")
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def setup_objet(db_session: Session):
    objet = Objet(codobj=1, name="Example Objet")
    db_session.add(objet)
    db_session.commit()
    db_session.refresh(objet)
    return objet

def test_get_all_objets(db_session: Session):
    response = client.get("/objets/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_objet_success(db_session: Session, setup_objet: Objet):
    response = client.get(f"/objets/{setup_objet.codobj}")
    assert response.status_code == 200
    assert response.json()["name"] == "Example Objet"

def test_get_objet_failure(db_session: Session):
    response = client.get("/objets/999")  # Non-existent ID
    assert response.status_code == 404

def test_create_objet_success(db_session: Session):
    objet_data = {"name": "New Objet"}
    response = client.post("/objets/", json=objet_data)
    assert response.status_code == 200
    assert response.json()["name"] == "New Objet"

def test_create_objet_failure(db_session: Session):
    # Example of failure: sending incomplete data
    objet_data = {}  # Required fields missing
    response = client.post("/objets/", json=objet_data)
    assert response.status_code == 422  # Unprocessable Entity

def test_update_objet_success(db_session: Session, setup_objet: Objet):
    update_data = {"name": "Updated Objet"}
    response = client.put(f"/objets/{setup_objet.codobj}", json=update_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Objet"

def test_update_objet_failure(db_session: Session):
    update_data = {"name": "Updated Objet"}
    response = client.put("/objets/999", json=update_data)  # Non-existent ID
    assert response.status_code == 404

def test_delete_objet_success(db_session: Session, setup_objet: Objet):
    response = client.delete(f"/objets/{setup_objet.codobj}")
    assert response.status_code == 200
    assert response.json()["codobj"] == setup_objet.codobj

def test_delete_objet_failure(db_session: Session):
    response = client.delete("/objets/999")  # Non-existent ID
    assert response.status_code == 404
