from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.client.Departement import Departement
from app.schemas.Departement import DepartementCreate, DepartementUpdate

def get_all_departements(skip: int, limit: int, db: Session):
    """
    Récupère tous les départements avec pagination
    """
    return db.query(Departement).offset(skip).limit(limit).all()

def get_departement(id: int, db: Session):
    """
    Récupère un département par son ID
    """
    departement = db.query(Departement).filter(Departement.id == id).first()
    if not departement:
        raise HTTPException(status_code=404, detail="Département non trouvé")
    return departement

def create_departement(departement: DepartementCreate, db: Session):
    """
    Crée un nouveau département
    """
    db_departement = Departement(**departement.dict())
    db.add(db_departement)
    db.commit()
    db.refresh(db_departement)
    return db_departement

def update_departement(id: int, departement_update: DepartementUpdate, db: Session):
    """
    Met à jour un département existant
    """
    db_departement = db.query(Departement).filter(Departement.id == id).first()
    if not db_departement:
        raise HTTPException(status_code=404, detail="Département non trouvé")

    for key, value in departement_update.dict(exclude_unset=True).items():
        setattr(db_departement, key, value)

    db.commit()
    db.refresh(db_departement)
    return db_departement

def delete_departement(id: int, db: Session):
    """
    Supprime un département
    """
    db_departement = db.query(Departement).filter(Departement.id == id).first()
    if not db_departement:
        raise HTTPException(status_code=404, detail="Département non trouvé")

    db.delete(db_departement)
    db.commit()
    return db_departement