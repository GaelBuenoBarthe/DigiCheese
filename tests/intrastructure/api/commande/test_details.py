import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.models.commande.detail import Detail
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
def create_test_detail(db_session: Session):
    test_detail = Detail(id=1, name="Test Detail", quantity=10)
    db_session.add(test_detail)
    db_session.commit()
    db_session.refresh(test_detail)
    return test_detail

def test_create_detail_success(db_session: Session):
    new_detail = {
        "id": 2,
        "name": "New Detail",
        "quantity": 20
    }
    response = client.post("/details/", json=new_detail)
    assert response.status_code == 201
    assert response.json()["id"] == 2

def test_create_detail_failure(db_session: Session):
    invalid_detail = {
        "id": "",  # Invalid id
        "name": "Invalid Detail",
        "quantity": 20
    }
    response = client.post("/details/", json=invalid_detail)
    assert response.status_code == 422

def test_get_detail_success(create_test_detail, db_session: Session):
    id = create_test_detail.id
    response = client.get(f"/details/{id}")
    assert response.status_code == 200
    assert response.json()["id"] == id

def test_get_detail_failure(db_session: Session):
    invalid_id = 9999
    response = client.get(f"/details/{invalid_id}")
    assert response.status_code == 404

def test_get_details_success(create_test_detail, db_session: Session):
    response = client.get("/details/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_details_empty(db_session: Session):
    response = client.get("/details/")
    assert response.status_code == 200
    assert len(response.json()) == 0

def test_update_detail_success(create_test_detail, db_session: Session):
    id = create_test_detail.id
    updated_data = {
        "name": "Updated Detail",
        "quantity": 30
    }
    response = client.put(f"/details/{id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Detail"

def test_update_detail_failure(db_session: Session):
    invalid_id = 9999
    updated_data = {
        "name": "Non-existent Detail",
        "quantity": 30
    }
    response = client.put(f"/details/{invalid_id}", json=updated_data)
    assert response.status_code == 404

def test_delete_detail_success(create_test_detail, db_session: Session):
    id = create_test_detail.id
    response = client.delete(f"/details/{id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Detail deleted successfully"}

    response = client.get(f"/details/{id}")
    assert response.status_code == 404

def test_delete_detail_failure(db_session: Session):
    invalid_id = 9999
    response = client.delete(f"/details/{invalid_id}")
    assert response.status_code == 404
