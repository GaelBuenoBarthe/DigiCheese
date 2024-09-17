from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Objet(Base):
    __tablename__ = "objet"

    codobj = Column(Integer, primary_key=True, index=True)
    libobj = Column(String(50), nullable=True)
    tailleobj = Column(String(50), nullable=True)
    puobj = Column(Numeric(precision=10, scale=4), default=0.0000)
    poidsobj = Column(Numeric(precision=10, scale=4), default=0.0000)
    indispobj = Column(Integer, default=0)
    o_imp = Column(Integer, default=0)
    o_aff = Column(Integer, default=0)
    o_cartp = Column(Integer, default=0)
    points = Column(Integer, default=0)
    o_ordre_aff = Column(Integer, default=0)

    conditionnement_id = Column(Integer, ForeignKey("conditionnement.idcondit"))
    conditionnement = relationship("Conditionnement", back_populates="objets")
    objet_conds = relationship("ObjetCond", back_populates="objet")

    def __repr__(self):
        return f"<Objet(codobj={self.codobj}, libobj={self.libobj}, tailleobj={self.tailleobj}, puobj={self.puobj}, poidsobj={self.poidsobj})>"
