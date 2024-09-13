from sqlalchemy import Column, Integer, String, Date, ForeignKey, Index, Float
from app.database import Base

#Creation de la table commande
class Commande(Base):
    __tablename__ = "t_entcde"

    codcde = Column(Integer, primary_key=True)
    datcde = Column(Date)
    codcli = Column(Integer, ForeignKey('t_client.codcli'))
    timbrecli = Column(Float)
    timbre_cde = Column(Float)
    nbcolis = Column(Integer, default=1)
    cheqcli = Column(Float)
    idcondit = Column(Integer, default=0)
    cdeComt = Column(String(255), default=None)
    barchive = Column(Integer, default=0)
    bstock = Column(Integer, default=0)

    __table_args__ = (Index('commmande_index', "cdeComt", "codcli"),)

    class Config:
        from_attributes = True