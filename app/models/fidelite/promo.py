from sqlalchemy import Column, Integer, String, Numeric
from app.database import Base

class Promo(Base):
    __tablename__ = "promo"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    discount_percentage = Column(Numeric(precision=5, scale=2))
    points_required = Column(Numeric(precision=10, scale=2))