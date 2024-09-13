from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.stock.objet import Objet
from app.schemas.objet import ObjetCreate, Objet as ObjetResponse

router = APIRouter()

# READ: Obtenir la liste des objets
@router.get("/", response_model=list[ObjetResponse])
def get_objects(db: Session, skip: int = 0, limit: int = 10):
    objects = db.query(Objet).offset(skip).limit(limit).all()
    return objects

# CREATE: Ajouter un nouvel objet
@router.post("/", response_model=ObjetResponse)
def create_object(object_create: ObjetCreate, db: Session):
    db_object = Objet(**object_create.dict())
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    return db_object

# READ: Obtenir un objet par ID
@router.get("/{object_id}", response_model=ObjetResponse)
def get_object(object_id: int, db: Session):
    db_object = db.query(Objet).filter(Objet.codobj == object_id).first()
    if not db_object:
        raise HTTPException(status_code=404, detail="Object not found")
    return db_object

# UPDATE: Mettre à jour un objet
@router.put("/{object_id}", response_model=ObjetResponse)
def update_object(object_id: int, object_update: ObjetCreate, db: Session):
    db_object = db.query(Objet).filter(Objet.codobj == object_id).first()
    if not db_object:
        raise HTTPException(status_code=404, detail="Object not found")

    for key, value in object_update.dict(exclude_unset=True).items():
        setattr(db_object, key, value)

    db.commit()
    db.refresh(db_object)
    return db_object

# DELETE: Supprimer un objet
@router.delete("/{object_id}", response_model=ObjetResponse)
def delete_object(object_id: int, db: Session):
    db_object = db.query(Objet).filter(Objet.codobj == object_id).first()
    if not db_object:
        raise HTTPException(status_code=404, detail="Object not found")

    db.delete(db_object)
    db.commit()
    return db_object
