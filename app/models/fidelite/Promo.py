from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.database import Base
class Promo(Base):
    __tablename__ = "t_promo"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    discount_percentage = Column(Numeric(precision=5, scale=2))
    points_required = Column(Numeric(precision=10, scale=2))

    def __init__(self, name: str, points_required: float):
        self.name = name
        self.points_required = points_required
