from http.client import HTTPException

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, base
from app.models.utilisateur import  role
from app.schemas.role import RoleCreate, RoleResponse
from app import crud

# Setup in-memory SQLite database
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def setup_database():
    base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    base.metadata.drop_all(bind=engine)


@pytest.fixture
def test_client():
    from fastapi.testclient import TestClient
    from app.main import app
    return TestClient(app)


def test_get_roles(setup_database):
    db = setup_database
    db.add(role(name="Admin"))
    db.add(role(name="User"))
    db.commit()

    roles = crud.get_roles(db)

    assert len(roles) == 2
    assert roles[0].name == "Admin"
    assert roles[1].name == "User"


def test_create_role(setup_database):
    db = setup_database
    role_data = RoleCreate(name="Manager")

    created_role = crud.create_role(db, role_data)

    assert created_role.name == "Manager"
    assert db.query(role).count() == 1


def test_create_role_invalid_data(setup_database):
    db = setup_database
    role_data = RoleCreate(name="")  # Assume empty name is invalid

    with pytest.raises(ValueError):
        crud.create_role(db, role_data)


def test_get_role(setup_database):
    db = setup_database
    db.add(role(name="Admin"))
    db.commit()

    created_role = db.query(role).first()
    fetched_role = crud.get_role(db, created_role.id)

    assert fetched_role.name == "Admin"


def test_get_role_not_found(setup_database):
    db = setup_database

    with pytest.raises(HTTPException) as excinfo:
        crud.get_role(db, 999)  # Non-existent role ID

    assert excinfo.value.status_code == 404


def test_delete_role(setup_database):
    db = setup_database
    db.add(role(name="Admin"))
    db.commit()

    created_role = db.query(role).first()
    deleted_role = crud.delete_role(db, created_role.id)

    assert deleted_role.name == "Admin"
    assert db.query(role).count() == 0


def test_delete_role_not_found(setup_database):
    db = setup_database

    with pytest.raises(HTTPException) as excinfo:
        crud.delete_role(db, 999)  # Non-existent role ID

    assert excinfo.value.status_code == 404
