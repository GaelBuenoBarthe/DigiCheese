from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Index, Numeric, Float,MetaData
from sqlalchemy.orm import relationship
from app.database import Base

class Role(Base):
	__tablename__ = "role"

	codrole= Column(Integer,primary_key=True)
	librole = Column(String(25), default=None)