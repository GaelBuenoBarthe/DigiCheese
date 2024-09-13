from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.role import RoleCreate, RoleResponse
from app.infrastructure.api.utilisateur.roles_controller import get_roles, create_role, get_role, delete_role

router = APIRouter()

@router.get("/", response_model=list[RoleResponse])
def read_roles( db: Session, skip: int = 0, limit: int = 10):
    return get_roles(skip, limit, db)

@router.post("/", response_model=RoleResponse)
def create_new_role(role: RoleCreate, db: Session):
    return create_role(role, db)

@router.get("/{role_id}", response_model=RoleResponse)
def read_role(role_id: int, db: Session):
    return get_role(role_id, db)

@router.delete("/{role_id}", response_model=RoleResponse)
def delete_existing_role(role_id: int, db: Session):
    return delete_role(role_id, db)
