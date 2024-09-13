from sqlalchemy.orm import Session
from app.models.commande.detail_objet import DetailObjet
from app.schemas.detail_objet import DetailObjetCreate

#Fonction pour créer un détail_objet
def create_detail_objet(db: Session, detail_objet: DetailObjetCreate):
    db_detail_objet = DetailObjet(**detail_objet.dict())
    db.add(db_detail_objet)
    db.commit()
    db.refresh(db_detail_objet)
    return db_detail_objet

#Fonction pour obtenir un détail_objet
def get_detail_objet(db: Session, id: int):
    return db.query(DetailObjet).filter(DetailObjet.id == id).first()

#Fonction pour obtenir tous les détails_objets
def get_detail_objets(db: Session, skip: int = 0, limit: int = 10):
    return db.query(DetailObjet).offset(skip).limit(limit).all()

#Fonction pour mettre à jour un détail_objet
def update_detail_objet(db: Session, id: int, detail_objet: DetailObjetCreate):
    db_detail_objet = db.query(DetailObjet).filter(DetailObjet.id == id).first()
    if db_detail_objet:
        for key, value in detail_objet.dict().items():
            setattr(db_detail_objet, key, value)
        db.commit()
        db.refresh(db_detail_objet)
    return db_detail_objet

#Fonction pour supprimer un détail_objet
def delete_detail_objet(db: Session, id: int):
    db_detail_objet = db.query(DetailObjet).filter(DetailObjet.id == id).first()
    if db_detail_objet:
        db.delete(db_detail_objet)
        db.commit()
    return db_detail_objet