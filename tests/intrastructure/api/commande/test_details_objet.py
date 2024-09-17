import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.models.commande.detail_objet import DetailObjet
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
def create_test_detail_objet(db_session: Session):
    test_detail_objet = DetailObjet(id=1, name="Test DetailObjet", quantity=10)
    db_session.add(test_detail_objet)
    db_session.commit()
    db_session.refresh(test_detail_objet)
    return test_detail_objet

def test_create_detail_objet_success(db_session: Session):
    new_detail_objet = {
        "id": 2,
        "name": "New DetailObjet",
        "quantity": 20
    }
    response = client.post("/detail_objets/", json=new_detail_objet)
    assert response.status_code == 201
    assert response.json()["id"] == 2

def test_create_detail_objet_failure(db_session: Session):
    invalid_detail_objet = {
        "id": "",  # Invalid id
        "name": "Invalid DetailObjet",
        "quantity": 20
    }
    response = client.post("/detail_objets/", json=invalid_detail_objet)
    assert response.status_code == 422

def test_get_detail_objet_success(create_test_detail_objet, db_session: Session):
    id = create_test_detail_objet.id
    response = client.get(f"/detail_objets/{id}")
    assert response.status_code == 200
    assert response.json()["id"] == id

def test_get_detail_objet_failure(db_session: Session):
    invalid_id = 9999
    response = client.get(f"/detail_objets/{invalid_id}")
    assert response.status_code == 404

def test_get_all_detail_objets_success(create_test_detail_objet, db_session: Session):
    response = client.get("/detail_objets/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_all_detail_objets_empty(db_session: Session):
    response = client.get("/detail_objets/")
    assert response.status_code == 200
    assert len(response.json()) == 0

def test_update_detail_objet_success(create_test_detail_objet, db_session: Session):
    id = create_test_detail_objet.id
    updated_data = {
        "name": "Updated DetailObjet",
        "quantity": 30
    }
    response = client.put(f"/detail_objets/{id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated DetailObjet"

def test_update_detail_objet_failure(db_session: Session):
    invalid_id = 9999
    updated_data = {
        "name": "Non-existent DetailObjet",
        "quantity": 30
    }
    response = client.put(f"/detail_objets/{invalid_id}", json=updated_data)
    assert response.status_code == 404

def test_delete_detail_objet_success(create_test_detail_objet, db_session: Session):
    id = create_test_detail_objet.id
    response = client.delete(f"/detail_objets/{id}")
    assert response.status_code == 200
    assert response.json() == {"message": "DetailObjet deleted successfully"}

    response = client.get(f"/detail_objets/{id}")
    assert response.status_code == 404

def test_delete_detail_objet_failure(db_session: Session):
    invalid_id = 9999
    response = client.delete(f"/detail_objets/{invalid_id}")
    assert response.status_code == 404
