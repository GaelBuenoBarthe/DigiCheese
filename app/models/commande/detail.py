from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Detail(Base):
    __tablename__ = "detailcde"

    id = Column(Integer, primary_key=True)
    detail_id = Column(Integer, index=True)  # Add detail_id
    objet_id = Column(Integer, index=True)   # Add objet_id
    codcde = Column(Integer, ForeignKey('commande.codcde'), index=True)
    qte = Column(Integer, default=1)
    colis = Column(Integer, default=1)
    commentaire = Column(String(100), default=None)
    name = Column(String(50))

    def __init__(self, detail_id: int, objet_id: int, codcde: int, qte: int, colis: int, commentaire: str, name: str):
        self.detail_id = detail_id
        self.objet_id = objet_id
        self.codcde = codcde
        self.qte = qte
        self.colis = colis
        self.commentaire = commentaire
        self.name = name

    class Config:
        from_attributes = True