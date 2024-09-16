from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.utilisateur import role
from app.schemas.utilisateur.role import RoleCreate


# Get all roles
def get_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(role).offset(skip).limit(limit).all()


# Create a new role
def create_role(db: Session, role_data: RoleCreate):
    db_role = role(**role_data.dict())
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
