from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.database import Base

class  ProgrammeFidelite(Base):
    __tablename__ = "programme_fidelite"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("client.codcli"))
    points = Column(Numeric(precision=10, scale=2), default=0)
    level = Column(String(50))  # Silver, Gold, etc.


