from http.client import HTTPException

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.main import app
from app.models.fidelite import programme_fidelite, transaction, bonus, promo
from app.schemas.programme_fidelite import TransactionCreate, BonusResponse, PromoResponse
from app import crud
from app.database import  Base

# Setup in-memory SQLite database
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def test_client():
    return TestClient(app)


def test_add_transaction(setup_database):
    db = setup_database
    user_id = 1
    db.add(programme_fidelite(user_id=user_id, points=0))
    db.commit()

    transaction_data = TransactionCreate(amount_spent=100)
    result = crud.add_transaction(user_id, transaction_data, db)

    assert result.points == 10
    assert db.query(transaction).count() == 1


def test_add_transaction_fidelity_not_found(setup_database):
    db = setup_database
    user_id = 1
    transaction_data = TransactionCreate(amount_spent=100)

    with pytest.raises(HTTPException) as excinfo:
        crud.add_transaction(user_id, transaction_data, db)

    assert excinfo.value.status_code == 404


def test_calculate_points():
    assert crud.calculate_points(100) == 10
    assert crud.calculate_points(0) == 0
    assert crud.calculate_points(50) == 5


def test_add_bonus(setup_database):
    db = setup_database
    user_id = 1
    db.add(programme_fidelite(user_id=user_id, points=0))
    db.commit()

    result = crud.add_bonus(user_id, "extra_points", 50, db)

    assert result.bonus_type == "extra_points"
    assert result.points == 50
    assert db.query(programme_fidelite).filter(programme_fidelite.user_id == user_id).first().points == 50


def test_add_bonus_fidelity_not_found(setup_database):
    db = setup_database
    user_id = 1

    with pytest.raises(HTTPException) as excinfo:
        crud.add_bonus(user_id, "extra_points", 50, db)

    assert excinfo.value.status_code == 404


def test_check_promo_eligibility(setup_database):
    db = setup_database
    user_id = 1
    db.add(programme_fidelite(user_id=user_id, points=100))
    db.add(promo(id=1, points_required=50))
    db.commit()

    result = crud.check_promo_eligibility(user_id, 1, db)

    assert result["eligible"] is True


def test_check_promo_eligibility_not_enough_points(setup_database):
    db = setup_database
    user_id = 1
    db.add(programme_fidelite(user_id=user_id, points=20))
    db.add(promo(id=1, points_required=50))
    db.commit()

    result = crud.check_promo_eligibility(user_id, 1, db)

    assert result["eligible"] is False
    assert result["message"] == "Not enough points"


def test_check_promo_eligibility_promo_not_found(setup_database):
    db = setup_database
    user_id = 1
    db.add(programme_fidelite(user_id=user_id, points=100))
    db.commit()

    with pytest.raises(HTTPException) as excinfo:
        crud.check_promo_eligibility(user_id, 1, db)

    assert excinfo.value.status_code == 404


def test_check_promo_eligibility_user_not_found(setup_database):
    db = setup_database
    db.add(promo(id=1, points_required=50))
    db.commit()

    with pytest.raises(HTTPException) as excinfo:
        crud.check_promo_eligibility(1, 1, db)

    assert excinfo.value.status_code == 404
