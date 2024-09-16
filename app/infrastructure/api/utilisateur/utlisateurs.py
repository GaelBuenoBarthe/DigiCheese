from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.utilisateur import utilisateur, role_utilisateur, role
from app.schemas.utilisateur import UtilisateurCreate, UtilisateurResponse, UtilisateurUpdate

router = APIRouter()

# Definition du CRUD
@router.get("/", response_model=list[UtilisateurResponse])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(SessionLocal)):
    users = db.query(utilisateur).offset(skip).limit(limit).all()
    return users

# Create a new user
@router.post("/", response_model=UtilisateurResponse)
def create_user(user: UtilisateurCreate, db: Session = Depends(SessionLocal)):
    db_user = utilisateur
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get user by ID
@router.get("/{user_id}", response_model=UtilisateurResponse)
def get_user(user_id: int, db: Session = Depends(SessionLocal)):
    user = db.query(utilisateur).filter(utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update user details
@router.put("/{user_id}", response_model=UtilisateurResponse)
def update_user(user_id: int, user_update: UtilisateurUpdate, db: Session = Depends(SessionLocal)):
    user = db.query(utilisateur).filter(utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update user fields
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user

# Delete a user by ID
@router.delete("/{user_id}", response_model=UtilisateurResponse)
def delete_user(user_id: int, db: Session = Depends(SessionLocal)):
    user = db.query(utilisateur).filter(utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return user

# Assign a role to a user
def assign_role_to_user(user_id: int, role_id: int, db: Session):
    user = db.query(utilisateur).filter(utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    role_to_assign = db.query(role).filter(role.id == role_id).first()
    if not role_to_assign:
        raise HTTPException(status_code=404, detail="Role not found")

    user_role = role_utilisateur(code_utilisateur=user_id, code_role=role_id)
    db.add(user_role)
    db.commit()
    return user

# Remove a role from a user
def remove_role_from_user(user_id: int, role_id: int, db: Session):
    user_role = db.query(role_utilisateur).filter(
        role_utilisateur.code_utilisateur == user_id,
        role_utilisateur.code_role == role_id
    ).first()
    if not user_role:
        raise HTTPException(status_code=404, detail="User role not found")

    db.delete(user_role)
    db.commit()
    return user_role