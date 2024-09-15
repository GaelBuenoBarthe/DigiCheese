from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Index, Numeric, Float,MetaData
from sqlalchemy.orm import relationship
from app.database import Base

class RoleUtilisateur(Base):
	__tablename__ = "utilisateur_role"

	id = Column(Integer,primary_key=True)
	utilisateur_id = Column(Integer, ForeignKey('utilisateur.code_utilisateur'))
	role_id = Column(Integer, ForeignKey('role.codrole'))