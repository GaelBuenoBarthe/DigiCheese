from pydantic import BaseModel

class Transaction(BaseModel):
    id: int
    user_id: int
    amount_spent: float
    points_earned: float
    name: str

    class Config:
        orm_mode = True