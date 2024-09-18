from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.utilisateur import role
from app.models.utilisateur.role import Role
from app.schemas.utilisateur.role import RoleCreate, RoleResponse


# Get all roles
def get_roles(skip: int, limit: int, db: Session):
    roles = db.query(Role).offset(skip).limit(limit).all()
    return [RoleResponse(id=role.codrole, name=role.librole) for role in roles]


# Create a new role
def create_role(db: Session, role_data: RoleCreate):
    db_role = role
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


# Get a role by ID
def get_role(db: Session, role_id: int):
    db_role = db.query(role).filter(role.id == role_id).first()
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role


# Delete a role by ID
def delete_role(db: Session, role_id: int):
    db_role = db.query(role).filter(role.id == role_id).first()
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    db.delete(db_role)
    db.commit()
    return db_role
