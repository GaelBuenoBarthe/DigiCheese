from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Client(Base):
    """
    Modèle SQLAlchemy représentant un client dans la base de données.
    """
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    genre = Column(String(8))
    nom = Column(String(40), index=True)
    prenom = Column(String(30))
    adresse1 = Column(String(50))
    adresse2 = Column(String(50))
    adresse3 = Column(String(50))
    ville_id = Column(Integer, ForeignKey("commune.id"))
    telephone = Column(String(10))
    email = Column(String(255))
    portable = Column(String(10))
    newsletter = Column(Boolean)
