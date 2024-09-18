# app/models/fidelite/programme_fidelite.py
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.fidelite.client_programme_fidelite import client_programme_fidelite

class ProgrammeFidelite(Base):
    __tablename__ = "programme_fidelite"

    id = Column(Integer, primary_key=True, index=True)
    points = Column(Numeric(precision=10, scale=2), default=0)
    level = Column(String(50))  # Silver, Gold, etc.

    clients = relationship("Client", secondary=client_programme_fidelite, back_populates="programmes_fidelite")

