from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.programme_fidelite import ProgrammeFideliteResponse, TransactionCreate, BonusResponse, PromoResponse
from app.infrastructure.api.fidelite.programmes_fidelite_controller import (add_transaction as add_transactionfromcontroller, add_bonus as add_bonusfromcontroller,
                                                                            check_promo_eligibility as check_promo_eligibilityfromcontroller)

router = APIRouter()

@router.post("/transactions", response_model=ProgrammeFideliteResponse)
def create_transaction(user_id: int, transaction_data: TransactionCreate, db: Session = Depends(get_db)) -> ProgrammeFideliteResponse:
    """
    Crée une transaction et retourne les informations du programme de fidélité.
    """
    return add_transactionfromcontroller(user_id, transaction_data, db)

@router.post("/bonus", response_model=BonusResponse)
def create_bonus(user_id: int, bonus_type: str, points: float, db: Session = Depends(get_db)) -> BonusResponse:
    """
    Crée un bonus pour un utilisateur et retourne les détails du bonus.
    """
    return add_bonusfromcontroller(user_id, bonus_type, points, db)

@router.get("/promo/{promo_id}", response_model=PromoResponse)
def check_promo(user_id: int, promo_id: int, db: Session = Depends(get_db)) -> PromoResponse:
    """
    Vérifie l'éligibilité d'une promotion pour un utilisateur et retourne les détails de la promo.
    """
    return check_promo_eligibilityfromcontroller(user_id, promo_id, db)
