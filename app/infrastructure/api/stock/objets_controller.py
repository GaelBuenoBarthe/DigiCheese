from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.stock.objet import Objet
from app.schemas.stocks.objet import ObjetCreate, ObjetUpdate

# Get all Objet entries
def get_all_objets(skip: int, limit: int, db: Session):
    return db.query(Objet).offset(skip).limit(limit).all()

# Get an Objet entry by ID
def get_objet(id: int, db: Session):
    objet = db.query(Objet).filter(Objet.codobj == id).first()
    if not objet:
        raise HTTPException(status_code=404, detail="Objet not found")
    return objet

# Create a new Objet entry
def create_objet(objet: ObjetCreate, db: Session):
    db_objet = Objet(**objet.dict())
    db.add(db_objet)
    db.commit()
    db.refresh(db_objet)
    return db_objet

# Update an existing Objet entry
def update_objet(id: int, objet_update: ObjetUpdate, db: Session):
    db_objet = db.query(Objet).filter(Objet.codobj == id).first()
    if not db_objet:
        raise HTTPException(status_code=404, detail="Objet not found")

    for key, value in objet_update.dict(exclude_unset=True).items():
        setattr(db_objet, key, value)

    db.commit()
    db.refresh(db_objet)
    return db_objet

# Delete an Objet entry
def delete_objet(id: int, db: Session):
    db_objet = db.query(Objet).filter(Objet.codobj == id).first()
    if not db_objet:
        raise HTTPException(status_code=404, detail="Objet not found")

    db.delete(db_objet)
    db.commit()
    return db_objet
