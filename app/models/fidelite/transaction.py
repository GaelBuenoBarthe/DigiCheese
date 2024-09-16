from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.database import Base
class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("client.codcli"))
    amount_spent = Column(Numeric(precision=10, scale=2))
    points_earned = Column(Numeric(precision=10, scale=2), default=0)


    client = relationship("client", back_populates="transactions")

    def __init__(self, user_id: int, amount_spent: float, points_earned: float):
        self.user_id = user_id
        self.amount_spent = amount_spent
        self.points_earned = points_earned