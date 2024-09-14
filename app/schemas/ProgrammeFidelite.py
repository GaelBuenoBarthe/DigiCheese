from pydantic import BaseModel
from typing import Optional

class TransactionCreate(BaseModel):
    amount_spent: float

class BonusResponse(BaseModel):
    id: int
    user_id: int
    bonus_type: str
    points: float

    class Config:
        orm_mode = True

class PromoResponse(BaseModel):
    id: int
    description: str
    points_required: int
    discount: float  # or any other field relevant to your promo

    class Config:
        orm_mode = True

class ProgrammeFideliteResponse(BaseModel):
    id: int
    user_id: int
    points: float

    class Config:
        orm_mode = True
