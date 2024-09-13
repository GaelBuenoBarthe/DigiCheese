from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List


from app.models.stock.objet import Objet
from app.schemas.objet import ObjetCreate, Objet as ObjetSchema

router = APIRouter()

# CREATE: Ajouter un nouvel objet
@router.post("/objets/", response_model=ObjetSchema)
def create_objet(objet: ObjetCreate, db: Session):
    db_objet = Objet(**objet.dict())
    db.add(db_objet)
    db.commit()
    db.refresh(db_objet)
    return db_objet

# READ: Obtenir la liste des objets
@router.get("/objets/", response_model=List[ObjetSchema])
def read_objets(db: Session, skip: int = 0, limit: int = 10):
    objets = db.query(Objet).offset(skip).limit(limit).all()
    return objets

# READ: Obtenir un objet par ID
@router.get("/objets/{codobj}", response_model=ObjetSchema)
def read_objet(codobj: int, db: Session):
    objet = db.query(Objet).filter(Objet.codobj == codobj).first()
    if objet is None:
        raise HTTPException(status_code=404, detail="Objet not found")
    return objet

# UPDATE: Mettre à jour un objet
@router.put("/objets/{codobj}", response_model=ObjetSchema)
def update_objet(codobj: int, objet_update: ObjetCreate, db: Session):
    db_objet = db.query(Objet).filter(Objet.codobj == codobj).first()
    if db_objet is None:
        raise HTTPException(status_code=404, detail="Objet not found")

    # Met à jour les attributs de l'objet
    for key, value in objet_update.dict().items():
        setattr(db_objet, key, value)

    db.commit()
    db.refresh(db_objet)
    return db_objet

# DELETE: Supprimer un objet
@router.delete("/objets/{codobj}", response_model=ObjetSchema)
def delete_objet(codobj: int, db: Session):
    db_objet = db.query(Objet).filter(Objet.codobj == codobj).first()
    if db_objet is None:
        raise HTTPException(status_code=404, detail="Objet not found")

    db.delete(db_objet)
    db.commit()
    return db_objet
