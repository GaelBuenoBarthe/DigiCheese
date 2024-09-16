from sqlalchemy.orm import Session
from app.models.client import departement
from app.schemas import departement as schemas

def get_departement(db: Session, departement_id: int):
    return db.query(departement).filter(departement_id == departement_id).first()

def get_departements(db: Session, skip: int = 0, limit: int = 10):
    return db.query(departement).offset(skip).limit(limit).all()

def create_departement(db: Session, departement: schemas.DepartementCreate):
    db_departement = departement
    db.add(db_departement)
    db.commit()
    db.refresh(db_departement)
    return db_departement

def update_departement(db: Session, departement_id: int, departement: schemas.DepartementUpdate):
    db_departement = db.query(departement).filter(departement_id == departement_id).first()
    if db_departement:
        for key, value in departement.dict().items():
            setattr(db_departement, key, value)
        db.commit()
        db.refresh(db_departement)
    return db_departement

def delete_departement(db: Session, departement_id: int):
    db_departement = db.query(departement).filter(departement_id == departement_id).first()
    if db_departement:
        db.delete(db_departement)
        db.commit()
    return db_departement