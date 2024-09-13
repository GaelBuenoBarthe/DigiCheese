from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Index, Numeric, Float,MetaData
from sqlalchemy.orm import relationship

from app.database import Base

class Conditionnement(Base):
	__tablename__ = "t_conditionnement"

	idcondit = Column(Integer,primary_key=True)
	libcondit = Column(String(50), default=None)
	poidscondit = Column(Integer)
	prixcond = Column(Numeric, default=0.0000)
	ordreimp = Column(Integer)
	# codobj = Column(Integer, ForeignKey('t_objet.codobj'))
	objets = relationship("ObjetCond",back_populates='condit')
