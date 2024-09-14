from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.utilisateur import UtilisateurCreate, UtilisateurResponse
from app.infrastructure.api.utilisateur.utilisateur_controller import get_users, create_user, get_user, update_user, delete_user

router = APIRouter()

@router.get("/", response_model=list[UtilisateurResponse])
def read_users(db: Session, skip: int = 0, limit: int = 10 ):
    return get_users(skip=skip, limit=limit, db=db)

@router.post("/", response_model=UtilisateurResponse)
def add_user(db: Session, user: UtilisateurCreate ):
    return create_user(user=user, db=db)

@router.get("/{user_id}", response_model=UtilisateurResponse)
def read_user(user_id: int, db: Session):
    return get_user(user_id=user_id, db=db)

@router.put("/{user_id}", response_model=UtilisateurResponse)
def edit_user(user_id: int, user_update: UtilisateurCreate, db: Session):
    return update_user(user_id=user_id, user_update=user_update, db=db)

@router.delete("/{user_id}", response_model=UtilisateurResponse)
def remove_user(user_id: int, db: Session):
    return delete_user(user_id=user_id, db=db)
