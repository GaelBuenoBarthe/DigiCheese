from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.utilisateur.role import Role
from app.models.utilisateur.role_utilisateur import RoleUtilisateur
from app.models.utilisateur.utilisateur import Utilisateur
from app.schemas.utilisateur.utilisateur import UtilisateurCreate, UtilisateurUpdate, UtilisateurResponse

# Trouver tous les utilisateurs
def get_users(db: Session, skip: int = 0, limit: int = 10):
    utilisateurs = db.query(Utilisateur).offset(skip).limit(limit).all()
    return [
        UtilisateurResponse(
            code_utilisateur=user.code_utilisateur,
            nom_utilisateur=user.nom_utilisateur,
            prenom_utilisateur=user.prenom_utilisateur,
            username=user.username,
            couleur_fond_utilisateur=user.couleur_fond_utilisateur,
            date_insc_utilisateur=user.date_insc_utilisateur
        )
        for user in utilisateurs
    ]

# Creer un utilisateur
def create_user(db: Session, user: UtilisateurCreate):
    db_user = Utilisateur(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UtilisateurResponse(
        code_utilisateur=db_user.code_utilisateur,
        nom_utilisateur=db_user.nom_utilisateur,
        prenom_utilisateur=db_user.prenom_utilisateur,
        username=db_user.username,
        couleur_fond_utilisateur=db_user.couleur_fond_utilisateur,
        date_insc_utilisateur=db_user.date_insc_utilisateur
    )

# Trouver un utilisateur par son ID
def get_user(db: Session, user_id: int):
    user = db.query(Utilisateur).filter(Utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return UtilisateurResponse(
        code_utilisateur=user.code_utilisateur,
        nom_utilisateur=user.nom_utilisateur,
        prenom_utilisateur=user.prenom_utilisateur,
        username=user.username,
        couleur_fond_utilisateur=user.couleur_fond_utilisateur,
        date_insc_utilisateur=user.date_insc_utilisateur
    )

# Mettre à jour un utilisateur
def update_user(db: Session, user_id: int, user_update: UtilisateurUpdate):
    user = db.query(Utilisateur).filter(Utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    # Mettre à jour les champs modifiés
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return UtilisateurResponse(
        code_utilisateur=user.code_utilisateur,
        nom_utilisateur=user.nom_utilisateur,
        prenom_utilisateur=user.prenom_utilisateur,
        username=user.username,
        couleur_fond_utilisateur=user.couleur_fond_utilisateur,
        date_insc_utilisateur=user.date_insc_utilisateur
    )

# Supprimer un utilisateur
def delete_user(db: Session, user_id: int):
    user = db.query(Utilisateur).filter(Utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Utisateur non trouvé")

    db.delete(user)
    db.commit()
    return UtilisateurResponse(
        code_utilisateur=user.code_utilisateur,
        nom_utilisateur=user.nom_utilisateur,
        prenom_utilisateur=user.prenom_utilisateur,
        username=user.username,
        couleur_fond_utilisateur=user.couleur_fond_utilisateur,
        date_insc_utilisateur=user.date_insc_utilisateur
    )

# Assigner un rôle à un utilisateur
def assign_role_to_user(db: Session, user_id: int, role_id: int):
    user = db.query(Utilisateur).filter(Utilisateur.code_utilisateur == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    role_to_assign = db.query(Role).filter(Role.id == role_id).first()
    if not role_to_assign:
        raise HTTPException(status_code=404, detail="Role non trouvé")

    user_role = RoleUtilisateur(code_utilisateur=user_id, code_role=role_id)
    db.add(user_role)
    db.commit()
    return UtilisateurResponse(
        code_utilisateur=user.code_utilisateur,
        nom_utilisateur=user.nom_utilisateur,
        prenom_utilisateur=user.prenom_utilisateur,
        username=user.username,
        couleur_fond_utilisateur=user.couleur_fond_utilisateur,
        date_insc_utilisateur=user.date_insc_utilisateur
    )

# Supprimer le rôle d'un utilisateur
def remove_role_from_user(db: Session, user_id: int, role_id: int):
    user_role = db.query(RoleUtilisateur).filter(
        RoleUtilisateur.code_utilisateur == user_id,
        RoleUtilisateur.code_role == role_id
    ).first()

    if not user_role:
        raise HTTPException(status_code=404, detail="Role non trouvé pour cet utilisateur")

    db.delete(user_role)
    db.commit()
    return UtilisateurResponse(
        code_utilisateur=user_role.code_utilisateur,
        nom_utilisateur=user_role.utilisateur.nom_utilisateur,
        prenom_utilisateur=user_role.utilisateur.prenom_utilisateur,
        username=user_role.utilisateur.username,
        couleur_fond_utilisateur=user_role.utilisateur.couleur_fond_utilisateur,
        date_insc_utilisateur=user_role.utilisateur.date_insc_utilisateur
    )
