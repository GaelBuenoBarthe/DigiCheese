from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

#Creation de la table detail
class Detail(Base):
    __tablename__ = "detailcde"

    id = Column(Integer, primary_key=True)
    codcde = Column(Integer, ForeignKey('commande.codcde'), index=True)
    qte = Column(Integer, default=1)
    colis = Column(Integer, default=1)
    commentaire = Column(String(100), default=None)

    class Config:
        from_attributes = True