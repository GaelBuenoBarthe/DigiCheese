from http.client import HTTPException

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from app.database import Base
from app.infrastructure.api.stock.conditionnements_controller import (
    create_conditionnement,
    get_conditionnements,
    get_conditionnement_by_id,
    update_conditionnement,
    delete_conditionnement
)
from app.schemas.stocks.conditionnements import ConditionnementCreate

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Setup the database
@pytest.fixture(scope="function")
def db():
    # Create the tables in the test database
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session  # Provide the session for the test
    session.close()
    Base.metadata.drop_all(bind=engine)

# Helper function to create a test conditionnement
def create_test_conditionnement_data():
    return ConditionnementCreate(
        libcondit="Conditionnement Test",
        poidscondit=100,
        prixcond=9.99,
        ordreimp=1
    )


# Test case for creating a conditionnement
def test_create_conditionnement(db: Session):
    conditionnement_data = create_test_conditionnement_data()

    conditionnement = create_conditionnement(db, conditionnement_data)

    assert conditionnement.idcondit is not None
    assert conditionnement.libcondit == "Conditionnement Test"
    assert conditionnement.poidscondit == 100
    assert conditionnement.prixcond == 9.99
    assert conditionnement.ordreimp == 1


# Test case for retrieving all conditionnements
def test_get_conditionnements(db: Session):
    # Pre-create some conditionnements
    conditionnement_data = create_test_conditionnement_data()
    create_conditionnement(db, conditionnement_data)
    create_conditionnement(db, conditionnement_data)

    conditionnements = get_conditionnements(db, skip=0, limit=10)

    assert len(conditionnements) == 2
    assert conditionnements[0].libcondit == "Conditionnement Test"


# Test case for retrieving a conditionnement by ID
def test_get_conditionnement_by_id(db: Session):
    conditionnement_data = create_test_conditionnement_data()
    conditionnement = create_conditionnement(db, conditionnement_data)

    retrieved = get_conditionnement_by_id(db, conditionnement.idcondit)

    assert retrieved.idcondit == conditionnement.idcondit
    assert retrieved.libcondit == "Conditionnement Test"


# Test case for updating a conditionnement
def test_update_conditionnement(db: Session):
    conditionnement_data = create_test_conditionnement_data()
    conditionnement = create_conditionnement(db, conditionnement_data)

    update_data = ConditionnementCreate(
        libcondit="Conditionnement Updated",
        poidscondit=150,
        prixcond=19.99,
        ordreimp=2
    )

    updated_conditionnement = update_conditionnement(db, conditionnement.idcondit, update_data)

    assert updated_conditionnement.idcondit == conditionnement.idcondit
    assert updated_conditionnement.libcondit == "Conditionnement Updated"
    assert updated_conditionnement.poidscondit == 150
    assert updated_conditionnement.prixcond == 19.99
    assert updated_conditionnement.ordreimp == 2


# Test case for deleting a conditionnement
def test_delete_conditionnement(db: Session):
    conditionnement_data = create_test_conditionnement_data()
    conditionnement = create_conditionnement(db, conditionnement_data)

    deleted_conditionnement = delete_conditionnement(db, conditionnement.idcondit)

    assert deleted_conditionnement.idcondit == conditionnement.idcondit
    assert deleted_conditionnement.libcondit == "Conditionnement Test"

    # Verify that the conditionnement no longer exists
    with pytest.raises(HTTPException):
        get_conditionnement_by_id(db, conditionnement.idcondit)
