from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Client(Base):
    """
    Modèle SQLAlchemy représentant un client dans la base de données.
    """
    __tablename__ = "client"  # Nom de la table

    codcli = Column(Integer, primary_key=True, index=True)  # Clé primaire, auto-incrémentée
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
    fidelite = Column(Integer, ForeignKey("programme_fidelite.id"))
    # Relation avec Commande (1-n)
    commandes = relationship("Commande", back_populates="client")
    commune = relationship("Commune", back_populates="clients")
    transactions = relationship("Transaction", back_populates="client")
    def __init__(self, genre: str, nom: str, prenom: str = None, adresse1: str = None, adresse2: str = None, adresse3: str = None, ville_id: int = None, telephone: str = None, email: str = None, portable: str = None, newsletter: bool = None):
        self.genre = genre
        self.nom = nom
        self.prenom = prenom
        self.adresse1 = adresse1
        self.adresse2 = adresse2
        self.adresse3 = adresse3
        self.ville_id = ville_id
        self.telephone = telephone
        self.email = email
        self.portable = portable
        self.newsletter = newsletter
