from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.utilisateur.role import RoleCreate, RoleResponse
from app.infrastructure.api.utilisateur.roles_controller import (create_role as create_rolefromcontroller,
                                                                 get_role as get_rolefromcontroller,
                                                                 delete_role as delete_rolefromcontroller, get_roles)

router = APIRouter()

@router.get("/", response_model=list[RoleResponse])
def read_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_roles(skip=skip, limit=limit, db=db)

@router.post("/", response_model=RoleResponse)
def create_new_role(role: RoleCreate, db: Session = Depends(get_db)):
    return create_rolefromcontroller(role, db)

@router.get("/{role_id}", response_model=RoleResponse)
def read_role(role_id: int, db: Session = Depends(get_db)):
    return get_rolefromcontroller(role_id, db)

@router.delete("/{role_id}", response_model=RoleResponse)
def delete_existing_role(role_id: int, db: Session = Depends(get_db)):
    return delete_rolefromcontroller(role_id, db)