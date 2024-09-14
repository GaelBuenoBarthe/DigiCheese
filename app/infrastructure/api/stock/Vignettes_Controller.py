from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.stock.Vignette import Vignette
from app.schemas.Vignette import VignetteCreate

# Get all Vignette entries
def get_all_vignettes(skip: int, limit: int, db: Session):
    return db.query(Vignette).offset(skip).limit(limit).all()

# Get a Vignette entry by ID
def get_vignette(id: int, db: Session):
    vignette = db.query(Vignette).filter(Vignette.id == id).first()
    if not vignette:
        raise HTTPException(status_code=404, detail="Vignette not found")
    return vignette

# Create a new Vignette entry
def create_vignette(vignette: VignetteCreate, db: Session):
    db_vignette = Vignette(**vignette.dict())
    db.add(db_vignette)
    db.commit()
    db.refresh(db_vignette)
    return db_vignette

# Update an existing Vignette entry
def update_vignette(id: int, vignette_update: VignetteCreate, db: Session):
    db_vignette = db.query(Vignette).filter(Vignette.id == id).first()
    if not db_vignette:
        raise HTTPException(status_code=404, detail="Vignette not found")

    for key, value in vignette_update.dict(exclude_unset=True).items():
        setattr(db_vignette, key, value)

    db.commit()
    db.refresh(db_vignette)
    return db_vignette

# Delete a Vignette entry
def delete_vignette(id: int, db: Session):
    db_vignette = db.query(Vignette).filter(Vignette.id == id).first()
    if not db_vignette:
        raise HTTPException(status_code=404, detail="Vignette not found")

    db.delete(db_vignette)
    db.commit()
    return db_vignette
