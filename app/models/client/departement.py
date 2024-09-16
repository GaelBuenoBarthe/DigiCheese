from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Departement(Base):
    """
    Modèle SQLAlchemy représentant un département dans la base de données
    """
    __tablename__ = "departement"

    id = Column(Integer, primary_key=True, index=True)  # Clé primaire, auto-incrémentée
    code = Column(String(50))  # Code du département
    nom = Column(String(50))  # Nom du département

    # Relation avec Commune (1-n)
    communes = relationship("Commune", back_populates="departement")