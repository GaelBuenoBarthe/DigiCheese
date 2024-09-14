from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.stock.Poids import Poids
from app.schemas.Poids import PoidsCreate

# Get all Poids entries
def get_all_poids(skip: int, limit: int, db: Session):
    return db.query(Poids).offset(skip).limit(limit).all()

# Get a Poids entry by ID
def get_poids(id: int, db: Session):
    poids = db.query(Poids).filter(Poids.id == id).first()
    if not poids:
        raise HTTPException(status_code=404, detail="Poids not found")
    return poids

# Create a new Poids entry
def create_poids(poids: PoidsCreate, db: Session):
    db_poids = Poids(**poids.dict())
    db.add(db_poids)
    db.commit()
    db.refresh(db_poids)
    return db_poids

# Update an existing Poids entry
def update_poids(id: int, poids_update: PoidsCreate, db: Session):
    db_poids = db.query(Poids).filter(Poids.id == id).first()
    if not db_poids:
        raise HTTPException(status_code=404, detail="Poids not found")

    for key, value in poids_update.dict(exclude_unset=True).items():
        setattr(db_poids, key, value)

    db.commit()
    db.refresh(db_poids)
    return db_poids

# Delete a Poids entry
def delete_poids(id: int, db: Session):
    db_poids = db.query(Poids).filter(Poids.id == id).first()
    if not db_poids:
        raise HTTPException(status_code=404, detail="Poids not found")

    db.delete(db_poids)
    db.commit()
    return db_poids
