from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Index, Numeric, Float,MetaData

from app.database import Base

class RoleUtilisateur(Base):
	__tablename__ = "t_utilisateur_role"

	id = Column(Integer,primary_key=True)
	utilisateur_id = Column(Integer, ForeignKey('t_utilisateur.code_utilisateur'))
	role_id = Column(Integer, ForeignKey('t_role.codrole'))