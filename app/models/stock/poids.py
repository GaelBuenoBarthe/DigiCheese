from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Index, Numeric, Float,MetaData

from app.database import Base

class Poids(Base):
	__tablename__ = "t_poids"

	id = Column(Integer,primary_key=True)
	valmin = Column(Numeric, default=0)
	valtimbre = Column(Numeric, default=0)