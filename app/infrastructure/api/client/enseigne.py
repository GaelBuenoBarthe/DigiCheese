from sqlalchemy.orm import Session
from app.models.client import enseigne as EnseigneModel
from app.schemas.client import enseigne as schemas


def get_enseigne(db: Session, enseigne_id: int):
    return db.query(EnseigneModel).filter(EnseigneModel.id == enseigne_id).first()

def get_enseignes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(EnseigneModel).offset(skip).limit(limit).all()

def create_enseigne(db: Session, enseigne: schemas.EnseigneCreate):
    db_enseigne = EnseigneModel
    db.add(db_enseigne)
    db.commit()
    db.refresh(db_enseigne)
    return db_enseigne

def update_enseigne(db: Session, enseigne_id: int, enseigne: schemas.EnseigneUpdate):
    db_enseigne = db.query(EnseigneModel).filter(EnseigneModel.id == enseigne_id).first()
    if db_enseigne:
        for key, value in enseigne.dict().items():
            setattr(db_enseigne, key, value)
        db.commit()
        db.refresh(db_enseigne)
    return db_enseigne

def delete_enseigne(db: Session, enseigne_id: int):
    db_enseigne = db.query(EnseigneModel).filter(EnseigneModel.id == enseigne_id).first()
    if db_enseigne:
        db.delete(db_enseigne)
        db.commit()
    return db_enseigne