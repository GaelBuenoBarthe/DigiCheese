import pytest
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

from app.database import SessionLocal
from app.main import app
from app.models.stock.vignette import Vignette
from app.schemas.vignette import VignetteCreate

client = TestClient(app)

@pytest.fixture(scope="module")
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def setup_vignette(db_session: Session):
    vignette = Vignette(id=1, description="Test Vignette")
    db_session.add(vignette)
    db_session.commit()
    db_session.refresh(vignette)
    return vignette

def test_get_all_vignettes(db_session: Session):
    response = client.get("/vignettes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_vignette_success(db_session: Session, setup_vignette: Vignette):
    response = client.get(f"/vignettes/{setup_vignette.id}")
    assert response.status_code == 200
    assert response.json()["description"] == "Test Vignette"

def test_get_vignette_failure(db_session: Session):
    response = client.get("/vignettes/999")  # Non-existent ID
    assert response.status_code == 404

def test_create_vignette_success(db_session: Session):
    vignette_data = {"description": "New Vignette"}
    response = client.post("/vignettes/", json=vignette_data)
    assert response.status_code == 200
    assert response.json()["description"] == "New Vignette"

def test_create_vignette_failure(db_session: Session):
    # Example of failure: sending incomplete data
    vignette_data = {}  # Required fields missing
    response = client.post("/vignettes/", json=vignette_data)
    assert response.status_code == 422  # Unprocessable Entity

def test_update_vignette_success(db_session: Session, setup_vignette: Vignette):
    update_data = {"description": "Updated Vignette"}
    response = client.put(f"/vignettes/{setup_vignette.id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["description"] == "Updated Vignette"

def test_update_vignette_failure(db_session: Session):
    update_data = {"description": "Updated Vignette"}
    response = client.put("/vignettes/999", json=update_data)  # Non-existent ID
    assert response.status_code == 404

def test_delete_vignette_success(db_session: Session, setup_vignette: Vignette):
    response = client.delete(f"/vignettes/{setup_vignette.id}")
    assert response.status_code == 200
    assert response.json()["id"] == setup_vignette.id

def test_delete_vignette_failure(db_session: Session):
    response = client.delete("/vignettes/999")  # Non-existent ID
    assert response.status_code == 404
