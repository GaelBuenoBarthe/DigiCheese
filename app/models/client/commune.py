from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Commune(Base):
    """
    Modèle SQLAlchemy représentant une commune dans la base de données.
    """
    __tablename__ = "commune"

    id = Column(Integer, primary_key=True, index=True)
    code_postal = Column(String(50))
    nom = Column(String(50))

    # Relation avec Departement (n-1)
    departement_id = Column(Integer, ForeignKey("departement.id"))
    departement = relationship("Departement", back_populates="communes")

    # Relation avec Client (1-n)
    clients = relationship("Client", back_populates="commune")