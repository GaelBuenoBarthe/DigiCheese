from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.client.enseigne import Enseigne
from app.schemas.client.enseigne import EnseigneCreate, EnseigneUpdate

def get_all_enseignes(skip: int, limit: int, db: Session):
    """
    Récupère toutes les enseignes avec pagination
    """
    return db.query(Enseigne).offset(skip).limit(limit).all()

def get_enseigne(id: int, db: Session):
    """
    Récupère une enseigne par son ID
    """
    enseigne = db.query(Enseigne).filter(Enseigne.id == id).first()
    if not enseigne:
        raise HTTPException(status_code=404, detail="Enseigne non trouvée")
    return enseigne

def create_enseigne(enseigne: EnseigneCreate, db: Session):
    """
    Crée une nouvelle enseigne
    """
    db_enseigne = Enseigne(**enseigne.dict())
    db.add(db_enseigne)
    db.commit()
    db.refresh(db_enseigne)
    return db_enseigne

def delete_enseigne(id: int, db: Session):
    """
    Supprime une enseigne existante.

    Args:
        id: ID de l'enseigne à supprimer.
        db: Session de base de données SQLAlchemy.

    Returns:
        L'enseigne supprimée.
    """
    db_enseigne = db.query(Enseigne).filter(Enseigne.id == id).first()
    if not db_enseigne:
        raise HTTPException(status_code=404, detail="Enseigne non trouvée")

    db.delete(db_enseigne)
    db.commit()
    return db_enseigne

def update_enseigne(id: int, enseigne_update: EnseigneUpdate, db: Session):
    """
    Met à jour une enseigne existante
    """
    db_enseigne = db.query(Enseigne).filter(Enseigne.id == id).first()
    if not db_enseigne:
        raise HTTPException(status_code=404, detail="Enseigne non trouvée")

    for key, value in enseigne_update.dict(exclude_unset=True).items():
        setattr(db_enseigne, key, value)

    db.commit