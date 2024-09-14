from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.client.commune import Commune
from app.schemas.commune import CommuneCreate, CommuneUpdate

def get_all_communes(skip: int, limit: int, db: Session):
    """
    Récupère toutes les communes avec pagination.
    """
    return db.query(Commune).offset(skip).limit(limit).all()

def get_commune(id: int, db: Session):
    """
    Récupère une commune par son ID.
    """
    commune = db.query(Commune).filter(Commune.id == id).first()
    if not commune:
        raise HTTPException(status_code=404, detail="Commune non trouvée")
    return commune

def create_commune(commune: CommuneCreate, db: Session):
    """
    Crée une nouvelle commune
    """
    db_commune = Commune(**commune.dict())
    db.add(db_commune)
    db.commit()
    db.refresh(db_commune)
    return db_commune

def update_commune(id: int, commune_update: CommuneUpdate, db: Session):
    """
    Met à jour une commune existante
    """
    db_commune = db.query(Commune).filter(Commune.id == id).first()
    if not db_commune:
        raise HTTPException(status_code=404, detail="Commune non trouvée")

    for key, value in commune_update.dict(exclude_unset=True).items():
        setattr(db_commune, key, value)

    db.commit()
    db.refresh(db_commune)
    return db_commune

def delete_commune(id: int, db: Session):
    """
    Supprime une commune
    """
    db_commune = db.query(Commune).filter(Commune.id == id).first()
    if not db_commune:
        raise HTTPException(status_code=404, detail="Commune non trouvée")

    db.delete(db_commune)
    db.commit()
    return db_commune