from tokenize import String

from sqlalchemy import Column, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from app.database import Base


class Bonus(Base):
    __tablename__ = "t_bonus"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("t_utilisateur.code_utilisateur"))
    bonus_type = Column(String(50))  # "WELCOME", "ANNIVERSARY"
    points = Column(Numeric(precision=10, scale=2))

    user = relationship("Utilisateur", back_populates="bonuses")

    def __init__(self, user_id: int, bonus_type: str, points: float):
        self.user_id = user_id
        self.bonus_type = bonus_type
        self.points = points