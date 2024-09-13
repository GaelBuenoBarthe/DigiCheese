from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.utilisateur import utilisateur
from app.schemas.utilisateur import UtilisateurCreate, UtilisateurResponse

router = APIRouter()

@router.get("/", response_model=list[UtilisateurResponse])
def get_users(db: Session, skip: int = 0, limit: int = 10 ):
    users = db.query(utilisateur).offset(skip).limit(limit).all()
    return users

@router.post("/", response_model=UtilisateurResponse)
def create_user(user: UtilisateurCreate, db: Session):
    db_user = utilisateur(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/{user_id}", response_model=UtilisateurResponse)
def get_user(user_id: int, db: Session):
    user = db.query(utilisateur).filter(utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UtilisateurResponse)
def update_user(user_id: int, user_update: UtilisateurCreate, db: Session):
    user = db.query(utilisateur).filter(utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user

@router.delete("/{user_id}", response_model=UtilisateurResponse)
def delete_user(user_id: int, db: Session):
    user = db.query(utilisateur).filter(utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return user
