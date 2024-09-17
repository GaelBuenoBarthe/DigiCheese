from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.utilisateur.role import Role
from app.models.utilisateur.role_utilisateur import RoleUtilisateur
from app.models.utilisateur.utilisateur import Utilisateur
from app.schemas.utilisateur import UtilisateurCreate, UtilisateurUpdate, UtilisateurResponse

# Get users from the database
def get_users(db: Session, skip: int = 0, limit: int = 10):
    utilisateurs = db.query(Utilisateur).offset(skip).limit(limit).all()
    return [
        UtilisateurResponse(
            id=user.code_utilisateur,
            name=user.nom_utilisateur,
            email=user.username
        )
        for user in utilisateurs
    ]

# Create a new user in the database
def create_user(db: Session, user: UtilisateurCreate):
    db_user = Utilisateur(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UtilisateurResponse(
        id=db_user.code_utilisateur,
        name=db_user.nom_utilisateur,
        email=db_user.username
    )

# Get a specific user by ID
def get_user(db: Session, user_id: int):
    user = db.query(Utilisateur).filter(Utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UtilisateurResponse(
        id=user.code_utilisateur,
        name=user.nom_utilisateur,
        email=user.username
    )

# Update user information
def update_user(db: Session, user_id: int, user_update: UtilisateurUpdate):
    user = db.query(Utilisateur).filter(Utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update user fields
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return UtilisateurResponse(
        id=user.code_utilisateur,
        name=user.nom_utilisateur,
        email=user.username
    )

# Delete a user from the database
def delete_user(db: Session, user_id: int):
    user = db.query(Utilisateur).filter(Utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return UtilisateurResponse(
        id=user.code_utilisateur,
        name=user.nom_utilisateur,
        email=user.username
    )

# Assign a role to a user
def assign_role_to_user(db: Session, user_id: int, role_id: int):
    user = db.query(Utilisateur).filter(Utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    role_to_assign = db.query(Role).filter(Role.id == role_id).first()
    if not role_to_assign:
        raise HTTPException(status_code=404, detail="Role not found")

    user_role = RoleUtilisateur(code_utilisateur=user_id, code_role=role_id)
    db.add(user_role)
    db.commit()
    return UtilisateurResponse(
        id=user.code_utilisateur,
        name=user.nom_utilisateur,
        email=user.username
    )

# Remove a role from a user
def remove_role_from_user(db: Session, user_id: int, role_id: int):
    user_role = db.query(RoleUtilisateur).filter(
        RoleUtilisateur.code_utilisateur == user_id,
        RoleUtilisateur.code_role == role_id
    ).first()

    if not user_role:
        raise HTTPException(status_code=404, detail="User role not found")

    db.delete(user_role)
    db.commit()
    return UtilisateurResponse(
        id=user_role.code_utilisateur,
        name=user_role.utilisateur.nom_utilisateur,
        email=user_role.utilisateur.username
    )
