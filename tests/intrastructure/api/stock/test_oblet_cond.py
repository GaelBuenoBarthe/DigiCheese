import pytest
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

from app.database import SessionLocal
from app.main import app
from app.models.stock.objet_cond import ObjetCond
from app.schemas.objet_cond import ObjetCondCreate

client = TestClient(app)

@pytest.fixture(scope="module")
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def setup_objet_cond(db_session: Session):
    objet_cond = ObjetCond(idrelcond=1, name="Example Cond")
    db_session.add(objet_cond)
    db_session.commit()
    db_session.refresh(objet_cond)
    return objet_cond

def test_get_all_objet_cond(db_session: Session):
    response = client.get("/objet_cond/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_objet_cond_success(db_session: Session, setup_objet_cond: ObjetCond):
    response = client.get(f"/objet_cond/{setup_objet_cond.idrelcond}")
    assert response.status_code == 200
    assert response.json()["name"] == "Example Cond"

def test_get_objet_cond_failure(db_session: Session):
    response = client.get("/objet_cond/999")  # Non-existent ID
    assert response.status_code == 404

def test_create_objet_cond_success(db_session: Session):
    objet_cond_data = {"name": "New Cond"}
    response = client.post("/objet_cond/", json=objet_cond_data)
    assert response.status_code == 200
    assert response.json()["name"] == "New Cond"

def test_create_objet_cond_failure(db_session: Session):
    # Example of failure: sending incomplete data
    objet_cond_data = {}  # Required fields missing
    response = client.post("/objet_cond/", json=objet_cond_data)
    assert response.status_code == 422  # Unprocessable Entity

def test_update_objet_cond_success(db_session: Session, setup_objet_cond: ObjetCond):
    update_data = {"name": "Updated Cond"}
    response = client.put(f"/objet_cond/{setup_objet_cond.idrelcond}", json=update_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Cond"

def test_update_objet_cond_failure(db_session: Session):
    update_data = {"name": "Updated Cond"}
    response = client.put("/objet_cond/999", json=update_data)  # Non-existent ID
    assert response.status_code == 404

def test_delete_objet_cond_success(db_session: Session, setup_objet_cond: ObjetCond):
    response = client.delete(f"/objet_cond/{setup_objet_cond.idrelcond}")
    assert response.status_code == 200
    assert response.json()["idrelcond"] == setup_objet_cond.idrelcond

def test_delete_objet_cond_failure(db_session: Session):
    response = client.delete("/objet_cond/999")  # Non-existent ID
    assert response.status_code == 404
