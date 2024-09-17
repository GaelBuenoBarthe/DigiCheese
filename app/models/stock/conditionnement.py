from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from app.database import Base

class Conditionnement(Base):
    __tablename__ = "conditionnement"

    idcondit = Column(Integer, primary_key=True)
    libcondit = Column(String(50), default=None)
    poidscondit = Column(Integer)
    prixcond = Column(Numeric, default=0.0000)
    ordreimp = Column(Integer)

    objets = relationship("Objet", back_populates="conditionnement")
    objet_conds = relationship("ObjetCond", back_populates="conditionnement")