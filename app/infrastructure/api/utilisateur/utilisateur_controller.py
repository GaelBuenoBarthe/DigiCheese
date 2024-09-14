from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.utilisateur import utilisateur, role_utilisateur, role
from app.schemas.utilisateur import UtilisateurCreate, UtilisateurUpdate, UtilisateurResponse


# Get users from the database
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(utilisateur).offset(skip).limit(limit).all()


# Create a new user in the database
def create_user(db: Session, user: UtilisateurCreate):
    db_user = utilisateur(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Get a specific user by ID
def get_user(db: Session, user_id: int):
    user = db.query(utilisateur).filter(utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# Update user information
def update_user(db: Session, user_id: int, user_update: UtilisateurUpdate):
    user = db.query(utilisateur).filter(utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update user fields
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user


# Delete a user from the database
def delete_user(db: Session, user_id: int):
    user = db.query(utilisateur).filter(utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return user


# Assign a role to a user
def assign_role_to_user(db: Session, user_id: int, role_id: int):
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
def remove_role_from_user(db: Session, user_id: int, role_id: int):
    user_role = db.query(role_utilisateur).filter(
        role_utilisateur.code_utilisateur == user_id,
        role_utilisateur.code_role == role_id
    ).first()

    if not user_role:
        raise HTTPException(status_code=404, detail="User role not found")

    db.delete(user_role)
    db.commit()
    return user_role
