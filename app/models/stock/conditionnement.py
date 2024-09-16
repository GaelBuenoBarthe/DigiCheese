from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship

from app.database import Base

class Conditionnement(Base):
    """
    Modèle SQLAlchemy représentant un conditionnement dans la base de données.
    """

    __tablename__ = "conditionnement"  # Nom de la table dans la base de données

    idcondit = Column(Integer, primary_key=True)  # Clé primaire de la table conditionnement
    libcondit = Column(String(50), default=None)  # Nom du conditionnement (libellé), taille maximale 50 caractères
    poidscondit = Column(Integer)  # Poids du conditionnement
    prixcond = Column(Numeric, default=0.0000)  # Prix associé au conditionnement, par défaut 0.0000
    ordreimp = Column(Integer)  # Ordre d'importance ou de priorité du conditionnement

    # Relation avec ObjetCond (1-n) : un conditionnement peut avoir plusieurs objets
    objets_cond = relationship("ObjetCond", back_populates="conditionnement")
