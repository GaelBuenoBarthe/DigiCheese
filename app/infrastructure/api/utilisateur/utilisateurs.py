from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import Utilisateur, RoleUtilisateur
from app.schemas.user import UtilisateurCreate, UtilisateurResponse, UtilisateurUpdate
from app.schemas.role import RoleAssignment

router = APIRouter()

# Get all users
@router.get("/", response_model=list[UtilisateurResponse])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(Utilisateur).offset(skip).limit(limit).all()
    return users

# Create a new user
@router.post("/", response_model=UtilisateurResponse)
def create_user(user: UtilisateurCreate, db: Session = Depends(get_db)):
    db_user = Utilisateur(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get user by ID
@router.get("/{user_id}", response_model=UtilisateurResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Utilisateur).filter(Utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update user details
@router.put("/{user_id}", response_model=UtilisateurResponse)
def update_user(user_id: int, user_update: UtilisateurUpdate, db: Session = Depends(get_db)):
    user = db.query(Utilisateur).filter(Utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update user fields
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user

# Assign role to user
@router.post("/{user_id}/assign-role", response_model=UtilisateurResponse)
def assign_role_to_user(user_id: int, role_assignment: RoleAssignment, db: Session = Depends(get_db)):
    user = db.query(Utilisateur).filter(Utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Create RoleUtilisateur entry
    role_user = RoleUtilisateur(utilisateur_id=user_id, role_id=role_assignment.role_id)
    db.add(role_user)
    db.commit()

    # Return the updated user
    db.refresh(user)
    return user

# Remove a role from a user (delete entry from RoleUtilisateur)
@router.delete("/{user_id}/remove-role/{role_id}", response_model=UtilisateurResponse)
def remove_role_from_user(user_id: int, role_id: int, db: Session = Depends(get_db)):
    role_user = db.query(RoleUtilisateur).filter(
        RoleUtilisateur.utilisateur_id == user_id,
        RoleUtilisateur.role_id == role_id
    ).first()

    if not role_user:
        raise HTTPException(status_code=404, detail="Role assignment not found")

    db.delete(role_user)
    db.commit()

    # Return the updated user
    user = db.query(Utilisateur).filter(Utilisateur.code_utilisateur == user_id).first()
    return user

# Delete a user by ID
@router.delete("/{user_id}", response_model=UtilisateurResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Utilisateur).filter(Utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return user
