from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Enseigne(Base):
    """
    Modèle SQLAlchemy représentant une enseigne dans la base de données
    """
    __tablename__ = "enseigne"

    id = Column(Integer, primary_key=True, index=True)  # Clé primaire, auto-incrémentée
    libelle = Column(String(50))  # Nom ou description de l'enseigne
    ville = Column(String(50))  # Ville où se situe l'enseigne
    departement_id = Column(Integer, ForeignKey("departement.id")) # Clé étrangère vers le département

    departement = relationship("Departement", back_populates="enseignes") # Relation avec le département