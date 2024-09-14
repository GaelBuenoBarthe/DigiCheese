from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Client(Base):
    """
    Modèle SQLAlchemy représentant un client dans la base de données.
    """
    __tablename__ = "clients"  # Nom de la table au pluriel

    id = Column(Integer, primary_key=True, index=True)  # Clé primaire, auto-incrémentée
    genre = Column(String(8))  # Genre du client (M/F/Autre, etc.)
    nom = Column(String(40), index=True)  # Nom de famille du client (indexé pour accélérer les recherches)
    prenom = Column(String(30))  # Prénom du client
    adresse1 = Column(String(50))  # Première ligne d'adresse
    adresse2 = Column(String(50))  # Deuxième ligne d'adresse (optionnelle)
    adresse3 = Column(String(50))  # Troisième ligne d'adresse (optionnelle)
    ville_id = Column(Integer, ForeignKey("commune.id"))  # Clé étrangère vers la commune
    telephone = Column(String(10))  # Numéro de téléphone
    email = Column(String(255))  # Adresse e-mail
    portable = Column(String(10))  # Numéro de portable
    newsletter = Column(Boolean)  # Abonnement à la newsletter (True/False)

    # Relation avec Commande (1-n)
    commandes = relationship("Commande", back_populates="client")