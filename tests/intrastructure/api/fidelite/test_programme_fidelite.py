import pytest
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from app.main import app
from app.models.fidelite import ProgrammeFidelite, Transaction, Bonus, Promo
from app.schemas.ProgrammeFidelite import TransactionCreate, BonusResponse, PromoResponse
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
def setup_fidelity_program(db_session: Session):
    user_fidelity = ProgrammeFidelite(user_id=1, points=100)
    db_session.add(user_fidelity)
    db_session.commit()
    db_session.refresh(user_fidelity)
    return user_fidelity

@pytest.fixture
def setup_promo(db_session: Session):
    promo = Promo(id=1, points_required=50)
    db_session.add(promo)
    db_session.commit()
    db_session.refresh(promo)
    return promo

@pytest.fixture
def setup_transaction(db_session: Session):
    transaction = Transaction(user_id=1, amount_spent=100, points_earned=10)
    db_session.add(transaction)
    db_session.commit()
    db_session.refresh(transaction)
    return transaction

@pytest.fixture
def setup_bonus(db_session: Session):
    bonus = Bonus(user_id=1, bonus_type="Holiday", points=20)
    db_session.add(bonus)
    db_session.commit()
    db_session.refresh(bonus)
    return bonus

def test_add_transaction_success(db_session: Session, setup_fidelity_program: ProgrammeFidelite):
    transaction_data = {"amount_spent": 200}
    response = client.post("/transactions/", json={"user_id": 1, **transaction_data})
    assert response.status_code == 200
    assert response.json()["points"] == 120  # Assuming initial points were 100 and 20 points are earned

def test_add_transaction_failure(db_session: Session):
    transaction_data = {"amount_spent": 200}
    response = client.post("/transactions/", json={"user_id": 999, **transaction_data})
    assert response.status_code == 404

def test_add_bonus_success(db_session: Session, setup_fidelity_program: ProgrammeFidelite):
    bonus_data = {"bonus_type": "Special", "points": 30}
    response = client.post("/bonuses/", json={"user_id": 1, **bonus_data})
    assert response.status_code == 200
    assert response.json()["points"] == 30

def test_add_bonus_failure(db_session: Session):
    bonus_data = {"bonus_type": "Special", "points": 30}
    response = client.post("/bonuses/", json={"user_id": 999, **bonus_data})
    assert response.status_code == 404

def test_check_promo_eligibility_success(db_session: Session, setup_fidelity_program: ProgrammeFidelite, setup_promo: Promo):
    response = client.get("/promos/1/eligibility", params={"user_id": 1})
    assert response.status_code == 200
    assert response.json()["eligible"] == True

def test_check_promo_eligibility_failure(db_session: Session, setup_fidelity_program: ProgrammeFidelite, setup_promo: Promo):
    response = client.get("/promos/1/eligibility", params={"user_id": 999})
    assert response.status_code == 404

def test_check_promo_eligibility_not_enough_points(db_session: Session, setup_fidelity_program: ProgrammeFidelite, setup_promo: Promo):
    db_session.query(ProgrammeFidelite).filter(ProgrammeFidelite.user_id == 1).update({ProgrammeFidelite.points: 30})
    db_session.commit()
    response = client.get("/promos/1/eligibility", params={"user_id": 1})
    assert response.status_code == 200
    assert response.json()["eligible"] == False
    assert response.json()["message"] == "Not enough points"
