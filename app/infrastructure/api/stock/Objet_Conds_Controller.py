from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.stock.Objet_Cond import ObjetCond
from app.schemas.objet_cond import ObjetCondCreate

# Get all ObjetCond entries
def get_all_objet_cond(skip: int, limit: int, db: Session):
    return db.query(ObjetCond).offset(skip).limit(limit).all()

# Get an ObjetCond by ID
def get_objet_cond(idrelcond: int, db: Session):
    objet_cond = db.query(ObjetCond).filter(ObjetCond.idrelcond == idrelcond).first()
    if not objet_cond:
        raise HTTPException(status_code=404, detail="ObjetCond not found")
    return objet_cond

# Create a new ObjetCond
def create_objet_cond(objet_cond: ObjetCondCreate, db: Session):
    db_objet_cond = ObjetCond(**objet_cond.dict())
    db.add(db_objet_cond)
    db.commit()
    db.refresh(db_objet_cond)
    return db_objet_cond

# Update an existing ObjetCond
def update_objet_cond(idrelcond: int, objet_cond_update: ObjetCondCreate, db: Session):
    db_objet_cond = db.query(ObjetCond).filter(ObjetCond.idrelcond == idrelcond).first()
    if not db_objet_cond:
        raise HTTPException(status_code=404, detail="ObjetCond not found")

    for key, value in objet_cond_update.dict(exclude_unset=True).items():
        setattr(db_objet_cond, key, value)

    db.commit()
    db.refresh(db_objet_cond)
    return db_objet_cond

# Delete an ObjetCond
def delete_objet_cond(idrelcond: int, db: Session):
    db_objet_cond = db.query(ObjetCond).filter(ObjetCond.idrelcond == idrelcond).first()
    if not db_objet_cond:
        raise HTTPException(status_code=404, detail="ObjetCond not found")

    db.delete(db_objet_cond)
    db.commit()
    return db_objet_cond
