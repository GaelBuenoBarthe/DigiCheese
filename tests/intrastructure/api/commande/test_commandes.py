import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.models.commande import Commande
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
def create_test_commande(db_session: Session):
    test_commande = Commande(codcde=1, description="Test Commande", montant=100.0)
    db_session.add(test_commande)
    db_session.commit()
    db_session.refresh(test_commande)
    return test_commande

def test_create_commande_success(db_session: Session):
    new_commande = {
        "codcde": 2,
        "description": "New Commande",
        "montant": 150.0
    }
    response = client.post("/commandes/", json=new_commande)
    assert response.status_code == 201
    assert response.json()["codcde"] == 2

def test_create_commande_failure(db_session: Session):
    invalid_commande = {
        "codcde": "",  # Invalid codcde
        "description": "Invalid Commande",
        "montant": 150.0
    }
    response = client.post("/commandes/", json=invalid_commande)
    assert response.status_code == 422

def test_get_commande_success(create_test_commande, db_session: Session):
    codcde = create_test_commande.codcde
    response = client.get(f"/commandes/{codcde}")
    assert response.status_code == 200
    assert response.json()["codcde"] == codcde

def test_get_commande_failure(db_session: Session):
    invalid_codcde = 9999
    response = client.get(f"/commandes/{invalid_codcde}")
    assert response.status_code == 404

def test_get_commandes_success(create_test_commande, db_session: Session):
    response = client.get("/commandes/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_commandes_empty(db_session: Session):
    response = client.get("/commandes/")
    assert response.status_code == 200
    assert len(response.json()) == 0

def test_update_commande_success(create_test_commande, db_session: Session):
    codcde = create_test_commande.codcde
    updated_data = {
        "description": "Updated Commande",
        "montant": 200.0
    }
    response = client.put(f"/commandes/{codcde}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["description"] == "Updated Commande"

def test_update_commande_failure(db_session: Session):
    invalid_codcde = 9999
    updated_data = {
        "description": "Non-existent Commande",
        "montant": 200.0
    }
    response = client.put(f"/commandes/{invalid_codcde}", json=updated_data)
    assert response.status_code == 404

def test_delete_commande_success(create_test_commande, db_session: Session):
    codcde = create_test_commande.codcde
    response = client.delete(f"/commandes/{codcde}")
    assert response.status_code == 200
    assert response.json() == {"message": "Commande deleted successfully"}

    response = client.get(f"/commandes/{codcde}")
    assert response.status_code == 404

def test_delete_commande_failure(db_session: Session):
    invalid_codcde = 9999
    response = client.delete(f"/commandes/{invalid_codcde}")
    assert response.status_code == 404
