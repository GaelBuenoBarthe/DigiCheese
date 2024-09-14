from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.database import Base

class  ProgrammeFidelite(Base):
    __tablename__ = "t_fidelity_program"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("t_utilisateur.code_utilisateur"))
    points = Column(Numeric(precision=10, scale=2), default=0)
    level = Column(String(50))  # Silver, Gold, etc.

    user = relationship("Utilisateur", back_populates="fidelity_program")
