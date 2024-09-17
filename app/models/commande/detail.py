from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

# Creation de la table detail
class Detail(Base):
    __tablename__ = "detailcde"

    id = Column(Integer, primary_key=True)
    codcde = Column(Integer, ForeignKey('commande.codcde'), index=True)
    qte = Column(Integer, default=1)
    colis = Column(Integer, default=1)
    commentaire = Column(String(100), default=None)
    name = Column(String(50))  # Ajout de la colonne name

    def __init__(self, codcde: int, qte: int, colis: int, commentaire: str, name: str):
        self.codcde = codcde
        self.qte = qte
        self.colis = colis
        self.commentaire = commentaire
        self.name = name  # Assignation de l'attribut name

    class Config:
        from_attributes = True