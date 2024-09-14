from sqlalchemy.orm import Session
from app.models.commande.Detail import Detail
from app.schemas.Detail import DetailCreate

def create_detail(db: Session, detail: DetailCreate):
    db_detail = Detail(**detail.dict())
    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)
    return db_detail

def get_detail(db: Session, id: int):
    return db.query(Detail).filter(Detail.id == id).first()

def get_details(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Detail).offset(skip).limit(limit).all()

def update_detail(db: Session, id: int, detail: DetailCreate):
    db_detail = db.query(Detail).filter(Detail.id == id).first()
    if db_detail:
        for key, value in detail.dict().items():
            setattr(db_detail, key, value)
        db.commit()
        db.refresh(db_detail)
    return db_detail

def delete_detail(db: Session, id: int):
    db_detail = db.query(Detail).filter(Detail.id == id).first()
    if db_detail:
        db.delete(db_detail)
        db.commit()
    return db_detail