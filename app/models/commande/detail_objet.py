from sqlalchemy import Column, Integer, ForeignKey, String
from app.database import Base

# Creation de la table detail_objet
class DetailObjet(Base):
    __tablename__ = "detailob"

    id = Column(Integer, primary_key=True)
    detail_id = Column(Integer, ForeignKey('detailcde.id'))
    objet_id = Column(Integer, ForeignKey('objet.codobj'))
    name = Column(String(50))  # Ajout de la colonne name

    def __init__(self, detail_id: int, objet_id: int, name: str):
        self.detail_id = detail_id
        self.objet_id = objet_id
        self.name = name

    class Config:
        from_attributes = True