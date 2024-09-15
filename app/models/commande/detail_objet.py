from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base

class DetailObjet(Base):
    __tablename__ = "detailob"

    id = Column(Integer, primary_key=True)
    detail_id = Column(Integer, ForeignKey('detailcde.id'))
    objet_id = Column(Integer, ForeignKey('objet.codobj'))

    class Config:
        from_attributes = True