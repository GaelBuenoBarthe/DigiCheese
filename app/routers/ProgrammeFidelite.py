from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.ProgrammeFidelite import ProgrammeFideliteResponse, TransactionCreate, BonusResponse, PromoResponse
from app.infrastructure.api.fidelite.Programmes_Fidelite_Controller import add_transaction, add_bonus, check_promo_eligibility

router = APIRouter()

@router.post("/transactions", response_model=ProgrammeFideliteResponse)
def create_transaction(user_id: int, transaction_data: TransactionCreate, db: Session = Depends(get_db)):
    return add_transaction(user_id, transaction_data, db)

@router.post("/bonus", response_model=BonusResponse)
def create_bonus(user_id: int, bonus_type: str, points: float, db: Session = Depends(get_db)):
    return add_bonus(user_id, bonus_type, points, db)

@router.get("/promo/{promo_id}", response_model=PromoResponse)
def check_promo(user_id: int, promo_id: int, db: Session = Depends(get_db)):
    return check_promo_eligibility(user_id, promo_id, db)
