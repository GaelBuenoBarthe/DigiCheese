from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Index, Numeric, Float,MetaData

from app.database import Base

class Commune(Base):
	__tablename__ = "t_communes"

	id = Column(Integer,primary_key=True)
	dep = Column(Integer,ForeignKey('t_dept.code_dept'))
	cp = Column(String(5), default=None)
	ville = Column(String(50), default=None)

	__table_args__ = (Index('commune_index', "dep", "cp", "ville"),)
