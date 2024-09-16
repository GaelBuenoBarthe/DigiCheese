from sqlalchemy import Column, Integer, String, Date, ForeignKey, Index, Float
from sqlalchemy.orm import relationship
from app.database import Base

#Creation de la table commande
class Commande(Base):
    __tablename__ = "commande"

    codcde = Column(Integer, primary_key=True)  # Clé primaire
    datcde = Column(Date)  # Date de la commande
    codcli = Column(Integer, ForeignKey('client.codcli'))  # ForeignKey vers Client
    timbrecli = Column(Float)  # Timbre client
    timbre_cde = Column(Float)  # Timbre commande
    nbcolis = Column(Integer, default=1)  # Nombre de colis
    cheqcli = Column(Float)  # Chèque client
    idcondit = Column(Integer, default=0)  # ID conditionnement
    cdeComt = Column(String(255), default=None)  # Commentaire commande
    barchive = Column(Integer, default=0)  # Archive
    bstock = Column(Integer, default=0)  # Stock

    # Relation vers Client (n-1)
    client = relationship("Client", back_populates="commandes")

    # Index sur certaines colonnes
    __table_args__ = (Index('commande_index', "cdeComt", "codcli"),)
