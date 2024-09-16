from sqlalchemy.orm import Session
from app.models.client import commune as CommuneModel
from app.schemas.client import commune as schemas


def get_commune(db: Session, commune_id: int):
    return db.query(CommuneModel).filter(CommuneModel.id == commune_id).first()

def get_communes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(CommuneModel).offset(skip).limit(limit).all()

def create_commune(db: Session, commune: schemas.CommuneCreate):
    db_commune = CommuneModel
    db.add(db_commune)
    db.commit()
    db.refresh(db_commune)
    return db_commune

def update_commune(db: Session, commune_id: int, commune: schemas.CommuneUpdate):
    db_commune = db.query(CommuneModel).filter(CommuneModel.id == commune_id).first()
    if db_commune:
        for key, value in commune.dict().items():
            setattr(db_commune, key, value)
        db.commit()
        db.refresh(db_commune)
    return db_commune

def delete_commune(db: Session, commune_id: int):
    db_commune = db.query(CommuneModel).filter(CommuneModel.id == commune_id).first()
    if db_commune:
        db.delete(db_commune)
        db.commit()
    return db_commune