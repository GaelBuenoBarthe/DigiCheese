from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.fidelite.client_programme_fidelite import client_programme_fidelite

class Client(Base):
    __tablename__ = 'client'

    codcli = Column(Integer, primary_key=True, nullable=False)
    genre = Column(String(8))
    nom = Column(String(40))
    prenom = Column(String(30))
    adresse1 = Column(String(50))
    adresse2 = Column(String(50))
    adresse3 = Column(String(50))
    ville_id = Column(Integer, ForeignKey('commune.id', name='fk_client_commune'))
    telephone = Column(String(10))
    email = Column(String(255))
    portable = Column(String(10))
    newsletter = Column(Boolean)

    # Defini la relation avec commune
    commune = relationship("Commune", back_populates="clients")

    # Defini la relation avec transaction
    transactions = relationship("Transaction", back_populates="client")

    # Defini la relation avec commande
    commandes = relationship("Commande", back_populates="client")

    # Defini la relation avec programme_fidelite
    programmes_fidelite = relationship("ProgrammeFidelite", secondary=client_programme_fidelite, back_populates="clients")