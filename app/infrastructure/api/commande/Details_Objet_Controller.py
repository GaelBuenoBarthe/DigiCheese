from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.commande.Detail_Objet import DetailObjet
from app.schemas.Detail_Objet import DetailObjetCreate

# Get all DetailObjet entries
def get_all_detail_objets(skip: int, limit: int, db: Session):
    return db.query(DetailObjet).offset(skip).limit(limit).all()

# Get a DetailObjet entry by ID
def get_detail_objet(id: int, db: Session):
    detail_objet = db.query(DetailObjet).filter(DetailObjet.id == id).first()
    if not detail_objet:
        raise HTTPException(status_code=404, detail="DetailObjet not found")
    return detail_objet

# Create a new DetailObjet entry
def create_detail_objet(detail_objet: DetailObjetCreate, db: Session):
    db_detail_objet = DetailObjet(**detail_objet.dict())
    db.add(db_detail_objet)
    db.commit()
    db.refresh(db_detail_objet)
    return db_detail_objet

# Update an existing DetailObjet entry
def update_detail_objet(id: int, detail_objet_update: DetailObjetCreate, db: Session):
    db_detail_objet = db.query(DetailObjet).filter(DetailObjet.id == id).first()
    if not db_detail_objet:
        raise HTTPException(status_code=404, detail="DetailObjet not found")

    for key, value in detail_objet_update.dict(exclude_unset=True).items():
        setattr(db_detail_objet, key, value)

    db.commit()
    db.refresh(db_detail_objet)
    return db_detail_objet

# Delete a DetailObjet entry
def delete_detail_objet(id: int, db: Session):
    db_detail_objet = db.query(DetailObjet).filter(DetailObjet.id == id).first()
    if not db_detail_objet:
        raise HTTPException(status_code=404, detail="DetailObjet not found")

    db.delete(db_detail_objet)
    db.commit()
    return db_detail_objet
