from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Commune(Base):
    """
    Modèle SQLAlchemy représentant une commune dans la base de données.
    """
    __tablename__ = "communes"

    id = Column(Integer, primary_key=True, index=True)  # Clé primaire, auto-incrémentée
    code_postal = Column(String)  # Code postal de la commune
    nom = Column(String)  # Nom de la commune

    # Relation avec Departement (n-1)
    departement_id = Column(Integer, ForeignKey("departement.id"))  # Clé étrangère vers le département
    departement = relationship("Departement", back_populates="communes")

    # Relation avec Client (1-n) - Même si pas explicitement dans le schéma, souvent utile
    clients = relationship("Client", back_populates="ville")