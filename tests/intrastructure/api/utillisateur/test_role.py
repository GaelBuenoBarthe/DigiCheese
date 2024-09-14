import pytest
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

from app.database import SessionLocal
from app.main import app
from app.models.utilisateur import role
from app.schemas.role import RoleCreate

client = TestClient(app)

@pytest.fixture(scope="module")
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def setup_role(db_session: Session):
    role = Role(id=1, role_name="Admin")
    db_session.add(role)
    db_session.commit()
    db_session.refresh(role)
    return role

def test_get_roles(db_session: Session):
    response = client.get("/roles/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_role_success(db_session: Session):
    role_data = {"role_name": "User"}
    response = client.post("/roles/", json=role_data)
    assert response.status_code == 200
    assert response.json()["role_name"] == "User"

def test_create_role_failure(db_session: Session):
    # Example of failure: sending incomplete data
    role_data = {}  # Required fields missing
    response = client.post("/roles/", json=role_data)
    assert response.status_code == 422  # Unprocessable Entity

def test_get_role_success(db_session: Session, setup_role: Role):
    response = client.get(f"/roles/{setup_role.id}")
    assert response.status_code == 200
    assert response.json()["role_name"] == "Admin"

def test_get_role_failure(db_session: Session):
    response = client.get("/roles/999")  # Non-existent role ID
    assert response.status_code == 404

def test_delete_role_success(db_session: Session, setup_role: Role):
    response = client.delete(f"/roles/{setup_role.id}")
    assert response.status_code == 200
    assert response.json()["id"] == setup_role.id

def test_delete_role_failure(db_session: Session):
    response = client.delete("/roles/999")  # Non-existent role ID
    assert response.status_code == 404
