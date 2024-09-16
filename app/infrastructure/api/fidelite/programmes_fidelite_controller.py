from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.fidelite import programme_fidelite, transaction, bonus, promo
from app.schemas.programme_fidelite import TransactionCreate, BonusResponse, PromoResponse

def add_transaction(user_id: int, transaction_data: TransactionCreate, db: Session):
    user_fidelity = db.query(programme_fidelite).filter(programme_fidelite.user_id == user_id).first()
    if not user_fidelity:
        raise HTTPException(status_code=404, detail="Fidelity program not found for user")

    points_earned = calculate_points(transaction_data.amount_spent)
    transaction_instance = transaction(user_id=user_id, amount_spent=transaction_data.amount_spent, points_earned=points_earned)

    user_fidelity.points += points_earned
    db.add(transaction_instance)
    db.commit()

    return user_fidelity

def calculate_points(amount: float) -> float:
    return amount * 0.1  # Example calculation: 10 points per 1 euro spent

def add_bonus(user_id: int, bonus_type: str, points: float, db: Session):
    user_fidelity = db.query(programme_fidelite).filter(programme_fidelite.user_id == user_id).first()
    if not user_fidelity:
        raise HTTPException(status_code=404, detail="Fidelity program not found for user")

    bonus_instance = bonus(user_id=user_id, bonus_type=bonus_type, points=points)
    user_fidelity.points += points

    db.add(bonus_instance)
    db.commit()
    return bonus_instance

def check_promo_eligibility(user_id: int, promo_id: int, db: Session):
    promo_instance = db.query(promo).filter(promo.id == promo_id).first()
    user_fidelity = db.query(programme_fidelite).filter(programme_fidelite.user_id == user_id).first()

    if not promo_instance or not user_fidelity:
        raise HTTPException(status_code=404, detail="Promo or user not found")

    if user_fidelity.points >= promo_instance.points_required:
        return {"eligible": True, "promo": promo_instance}
    else:
        return {"eligible": False, "message": "Not enough points"}
