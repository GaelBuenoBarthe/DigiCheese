from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Index, Numeric, Float,MetaData

from app.database import Base

class Departement(Base):
	__tablename__ = "t_dept"

	code_dept = Column(String(2),primary_key=True)
	nom_dept = Column(String(50), default=None)
	ordre_aff_dept = Column(Integer, default=0)
