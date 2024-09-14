import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.database import get_db, Base
from app.models.client.enseigne import Enseigne
from app.schemas.enseigne import EnseigneCreate, EnseigneUpdate
from app.database import SessionLocal, engine

# Configure TestClient
client = TestClient(app)

# Création de la base de données pour les tests
Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def db_session():
    """
    Crée une session de test de la base de données.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def create_test_enseigne(db_session: Session):
    """
    Crée une enseigne pour les tests.
    """
    test_enseigne = Enseigne(name="Test Enseigne")
    db_session.add(test_enseigne)
    db_session.commit()
    db_session.refresh(test_enseigne)
    return test_enseigne

### tests CRUD Enseigne

# Teste la création d'une enseigne
def test_create_enseigne_success(db_session: Session):
    """
    Teste la création réussie d'une nouvelle enseigne.
    """
    new_enseigne = {
        "name": "New Enseigne"
    }
    response = client.post("/enseignes/", json=new_enseigne)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "New Enseigne"

def test_create_enseigne_failure(db_session: Session):
    """
    Teste la création échouée d'une enseigne avec des données invalides.
    """
    invalid_enseigne = {
        "name": ""  # Nom invalide (vide)
    }
    response = client.post("/enseignes/", json=invalid_enseigne)
    assert response.status_code == 422  # Unprocessable Entity (FastAPI validation)

# Teste la récupération d'une enseigne
def test_get_enseigne_success(create_test_enseigne, db_session: Session):
    """
    Teste la récupération réussie d'une enseigne par son ID.
    """
    enseigne_id = create_test_enseigne.id
    response = client.get(f"/enseignes/{enseigne_id}")
    assert response.status_code == 200
    assert response.json()["id"] == enseigne_id

def test_get_enseigne_failure(db_session: Session):
    """
    Teste la récupération échouée d'une enseigne avec un ID invalide.
    """
    invalid_enseigne_id = 9999  # Un ID qui n'existe pas
    response = client.get(f"/enseignes/{invalid_enseigne_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Enseigne non trouvée"

# Teste la mise à jour d'une enseigne
def test_update_enseigne_success(create_test_enseigne, db_session: Session):
    """
    Teste la mise à jour réussie d'une enseigne existante.
    """
    enseigne_id = create_test_enseigne.id
    updated_data = {
        "name": "Updated Enseigne"
    }
    response = client.put(f"/enseignes/{enseigne_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Enseigne"

def test_update_enseigne_failure(db_session: Session):
    """
    Teste la mise à jour échouée d'une enseigne avec un ID invalide.
    """
    invalid_enseigne_id = 9999  # Un ID qui n'existe pas
    updated_data = {
        "name": "Non-existent Enseigne"
    }
    response = client.put(f"/enseignes/{invalid_enseigne_id}", json=updated_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Enseigne non trouvée"

# Teste la suppression d'une enseigne
def test_delete_enseigne_success(create_test_enseigne, db_session: Session):
    """
    Teste la suppression réussie d'une enseigne.
    """
    enseigne_id = create_test_enseigne.id
    response = client.delete(f"/enseignes/{enseigne_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Enseigne deleted successfully"}

    # Vérifie que l'enseigne n'existe plus après suppression
    response = client.get(f"/enseignes/{enseigne_id}")
    assert response.status_code == 404

def test_delete_enseigne_failure(db_session: Session):
    """
    Teste la suppression échouée d'une enseigne avec un ID invalide.
    """
    invalid_enseigne_id = 9999  # Un ID qui n'existe pas
    response = client.delete(f"/enseignes/{invalid_enseigne_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Enseigne non trouvée"

# Teste la récupération de toutes les enseignes
def test_get_all_enseignes_success(create_test_enseigne, db_session: Session):
    """
    Teste la récupération réussie de toutes les enseignes.
    """
    response = client.get("/enseignes/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_all_enseignes_empty(db_session: Session):
    """
    Teste la récupération lorsque aucune enseigne n'est disponible.
    """
    response = client.get("/enseignes/")
    assert response.status_code == 200
    assert len(response.json()) == 0
