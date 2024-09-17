from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.client.commune import Commune
from app.schemas.client.commune import CommuneCreate, CommuneUpdate

def get_all_communes(skip: int, limit: int, db: Session):
    return db.query(Commune).offset(skip).limit(limit).all()

def get_commune(id: int, db: Session):
    commune = db.query(Commune).filter(Commune.id == id).first()
    if not commune:
        raise HTTPException(status_code=404, detail="Commune non trouvée")
    return commune

def create_commune(commune: CommuneCreate, db: Session):
    db_commune = Commune(**commune.model_dump())
    db.add(db_commune)
    db.commit()
    db.refresh(db_commune)
    return db_commune

def update_commune(id: int, commune_update: CommuneUpdate, db: Session):
    db_commune = db.query(Commune).filter(Commune.id == id).first()
    if not db_commune:
        raise HTTPException(status_code=404, detail="Commune non trouvée")

    for key, value in commune_update.model_dump(exclude_unset=True).items():
        setattr(db_commune, key, value)

    db.commit()
    db.refresh(db_commune)
    return db_commune

def delete_commune(id: int, db: Session):
    db_commune = db.query(Commune).filter(Commune.id == id).first()
    if not db_commune:
        raise HTTPException(status_code=404, detail="Commune non trouvée")

    db.delete(db_commune)
    db.commit()
    return db_commune
