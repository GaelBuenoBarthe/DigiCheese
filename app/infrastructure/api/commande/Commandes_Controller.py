from sqlalchemy.orm import Session
from app.models.commande import Commande
from app.schemas.Commande import CommandeCreate

def create_commande(db: Session, commande: CommandeCreate):
    db_commande = Commande(**commande.dict())
    db.add(db_commande)
    db.commit()
    db.refresh(db_commande)
    return db_commande

def get_commande(db: Session, codcde: int):
    return db.query(Commande).filter(Commande.codcde == codcde).first()

def get_commandes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Commande).offset(skip).limit(limit).all()

def update_commande(db: Session, codcde: int, commande: CommandeCreate):
    db_commande = db.query(Commande).filter(Commande.codcde == codcde).first()
    if db_commande:
        for key, value in commande.dict().items():
            setattr(db_commande, key, value)
        db.commit()
        db.refresh(db_commande)
    return db_commande

def delete_commande(db: Session, codcde: int):
    db_commande = db.query(Commande).filter(Commande.codcde == codcde).first()
    if db_commande:
        db.delete(db_commande)
        db.commit()
    return db_commande