from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class ObjetCond(Base):
    __tablename__ = "t_rel_cond"

    idrelcond = Column(Integer, primary_key=True, index=True)
    qteobjdeb = Column(Integer, default=0)
    qteobjfin = Column(Integer, default=0)
    codobj = Column(Integer, ForeignKey('objet.codobj'))
    codcond = Column(Integer, ForeignKey('conditionnement.idcondit'))

    objet = relationship("Objet", back_populates="objet_conds")
    conditionnement = relationship("Conditionnement", back_populates="objet_conds")
