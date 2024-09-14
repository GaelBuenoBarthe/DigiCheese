import pytest
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

from app.database import SessionLocal
from app.main import app
from app.models.utilisateur import Utilisateur, Role_Utilisateur, Role
from app.schemas.Utilisateur import UtilisateurCreate, UtilisateurUpdate

client = TestClient(app)

@pytest.fixture(scope="module")
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def setup_user(db_session: Session):
    user = Utilisateur(code_utilisateur=1, name="John Doe")
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user

@pytest.fixture
def setup_role(db_session: Session):
    role = Role(id=1, role_name="Admin")
    db_session.add(role)
    db_session.commit()
    db_session.refresh(role)
    return role

@pytest.fixture
def setup_user_role(db_session: Session, setup_user: Utilisateur, setup_role: Role):
    user_role = Role_Utilisateur(code_utilisateur=setup_user.code_utilisateur, code_role=setup_role.id)
    db_session.add(user_role)
    db_session.commit()
    db_session.refresh(user_role)
    return user_role

def test_get_users(db_session: Session):
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user_success(db_session: Session):
    user_data = {"name": "Jane Doe"}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"

def test_create_user_failure(db_session: Session):
    # Example of failure: sending incomplete data
    user_data = {}  # Required fields missing
    response = client.post("/users/", json=user_data)
    assert response.status_code == 422  # Unprocessable Entity

def test_get_user_success(db_session: Session, setup_user: Utilisateur):
    response = client.get(f"/users/{setup_user.code_utilisateur}")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_get_user_failure(db_session: Session):
    response = client.get("/users/999")  # Non-existent user ID
    assert response.status_code == 404

def test_update_user_success(db_session: Session, setup_user: Utilisateur):
    update_data = {"name": "John Smith"}
    response = client.put(f"/users/{setup_user.code_utilisateur}", json=update_data)
    assert response.status_code == 200
    assert response.json()["name"] == "John Smith"

def test_update_user_failure(db_session: Session):
    update_data = {"name": "John Smith"}
    response = client.put("/users/999", json=update_data)  # Non-existent user ID
    assert response.status_code == 404

def test_delete_user_success(db_session: Session, setup_user: Utilisateur):
    response = client.delete(f"/users/{setup_user.code_utilisateur}")
    assert response.status_code == 200
    assert response.json()["code_utilisateur"] == setup_user.code_utilisateur

def test_delete_user_failure(db_session: Session):
    response = client.delete("/users/999")  # Non-existent user ID
    assert response.status_code == 404

def test_assign_role_to_user_success(db_session: Session, setup_user: Utilisateur, setup_role: Role):
    response = client.post(f"/users/{setup_user.code_utilisateur}/roles/{setup_role.id}")
    assert response.status_code == 200
    assert len(db_session.query(Role_Utilisateur).all()) > 0  # Check if role is assigned

def test_assign_role_to_user_failure(db_session: Session):
    response = client.post("/users/999/roles/1")  # Non-existent user ID
    assert response.status_code == 404

def test_remove_role_from_user_success(db_session: Session, setup_user_role: Role_Utilisateur):
    response = client.delete(f"/users/{setup_user_role.code_utilisateur}/roles/{setup_user_role.code_role}")
    assert response.status_code == 200
    assert len(db_session.query(Role_Utilisateur).all()) == 0  # Check if role is removed

def test_remove_role_from_user_failure(db_session: Session):
    response = client.delete("/users/999/roles/1")  # Non-existent user ID
    assert response.status_code == 404
