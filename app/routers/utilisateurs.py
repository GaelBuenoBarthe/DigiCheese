from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UtilisateurCreate, UtilisateurResponse, UtilisateurUpdate
from app.schemas.role import RoleAssignment
from app.controllers.user_controller import create_user, get_users, get_user, update_user, delete_user, assign_role_to_user, remove_role_from_user

router = APIRouter()

@router.get("/", response_model=list[UtilisateurResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_users(skip, limit, db)

@router.post("/", response_model=UtilisateurResponse)
def create_new_user(user: UtilisateurCreate, db: Session = Depends(get_db)):
    return create_user(user, db)

@router.get("/{user_id}", response_model=UtilisateurResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(user_id, db)

@router.put("/{user_id}", response_model=UtilisateurResponse)
def update_existing_user(user_id: int, user_update: UtilisateurUpdate, db: Session = Depends(get_db)):
    return update_user(user_id, user_update, db)

@router.post("/{user_id}/assign-role", response_model=UtilisateurResponse)
def assign_role(user_id: int, role_assignment: RoleAssignment, db: Session = Depends(get_db)):
    return assign_role_to_user(user_id, role_assignment, db)

@router.delete("/{user_id}", response_model=UtilisateurResponse)
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user(user_id, db)

@router.delete("/{user_id}/remove-role/{role_id}", response_model=UtilisateurResponse)
def remove_role(user_id: int, role_id: int, db: Session = Depends(get_db)):
    return remove_role_from_user(user_id, role_id, db)
