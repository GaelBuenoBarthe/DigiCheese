from sqlalchemy.orm import Session
from app.models.commande.detail import Detail
from app.schemas.commande.detail import DetailCreate

#Fonction pour créer un détail
def create_detail(db: Session, detail: DetailCreate):
    db_detail = Detail(**detail.dict())
    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)
    return db_detail

#Fonction pour obtenir un détail
def get_detail(db: Session, id: int):
    return db.query(Detail).filter(Detail.id == id).first()

#Fonction pour obtenir tous les détails
def get_details(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Detail).offset(skip).limit(limit).all()

#Fonction pour mettre à jour un détail
def update_detail(db: Session, id: int, detail: DetailCreate):
    db_detail = db.query(Detail).filter(Detail.id == id).first()
    if db_detail:
        for key, value in detail.dict().items():
            setattr(db_detail, key, value)
        db.commit()
        db.refresh(db_detail)
    return db_detail

#Fonction pour supprimer un détail
def delete_detail(db: Session, id: int):
    db_detail = db.query(Detail).filter(Detail.id == id).first()
    if db_detail:
        db.delete(db_detail)
        db.commit()
    return db_detail