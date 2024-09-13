from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.utilisateur import role
from app.schemas.role import RoleCreate, RoleResponse

router = APIRouter()


# Get all roles
@router.get("/", response_model=list[RoleResponse])
def get_roles(db: Session, skip: int = 0, limit: int = 10 ):
    roles = db.query(role).offset(skip).limit(limit).all()
    return roles


# Create a new role
@router.post("/", response_model=RoleResponse)
def create_role(role: RoleCreate, db: Session):
    db_role = role(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


# Get role by ID
@router.get("/{role_id}", response_model=RoleResponse)
def get_role(role_id: int, db: Session, role= role):
    role = db.query(role).filter(role.codrole == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


# Delete a role by ID
@router.delete("/{role_id}", response_model=RoleResponse)
def delete_role(role_id: int, db: Session, role=role):
    role = db.query(role).filter(role.codrole == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    db.delete(role)
    db.commit()
    return role
