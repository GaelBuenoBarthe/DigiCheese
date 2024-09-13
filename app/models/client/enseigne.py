from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Enseigne(Base):
    """
    Modèle SQLAlchemy représentant une enseigne dans la base de données
    """
    __tablename__ = "enseigne"

    id = Column(Integer, primary_key=True, index=True)
    libelle = Column(String(50))
    ville = Column(String(50))
    departement_id = Column(Integer, ForeignKey("departement.id"))
    departement = relationship("Departement", back_populates="enseignes")