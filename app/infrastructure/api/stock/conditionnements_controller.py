from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.stock.conditionnement import Conditionnement
from app.schemas.stock.conditionnements import ConditionnementCreate

# Fonction pour créer un nouveau conditionnement
def create_conditionnement(db: Session, conditionnement_data: ConditionnementCreate):
    """
    Crée un nouveau conditionnement dans la base de données.
    """
    nouveau_conditionnement = Conditionnement(**conditionnement_data.dict())
    db.add(nouveau_conditionnement)
    db.commit()
    db.refresh(nouveau_conditionnement)
    return nouveau_conditionnement

# Fonction pour récupérer tous les conditionnements
def get_conditionnements(db: Session, skip: int = 0, limit: int = 10):
    """
    Récupère une liste de conditionnements avec pagination.
    """
    return db.query(Conditionnement).offset(skip).limit(limit).all()

# Fonction pour récupérer un conditionnement par son ID
def get_conditionnement_by_id(db: Session, idcondit: int):
    """
    Récupère un conditionnement spécifique par son ID.
    """
    conditionnement = db.query(Conditionnement).filter(Conditionnement.idcondit == idcondit).first()
    if not conditionnement:
        raise HTTPException(status_code=404, detail="Conditionnement non trouvé")
    return conditionnement

# Fonction pour mettre à jour un conditionnement existant
def update_conditionnement(db: Session, idcondit: int, conditionnement_data: ConditionnementCreate):
    """
    Met à jour les informations d'un conditionnement existant.
    """
    conditionnement = db.query(Conditionnement).filter(Conditionnement.idcondit == idcondit).first()
    if not conditionnement:
        raise HTTPException(status_code=404, detail="Conditionnement non trouvé")

    # Mise à jour des champs avec les nouvelles données
    for key, value in conditionnement_data.dict(exclude_unset=True).items():
        setattr(conditionnement, key, value)

    db.commit()
    db.refresh(conditionnement)
    return conditionnement

# Fonction pour supprimer un conditionnement par son ID
def delete_conditionnement(db: Session, idcondit: int):
    """
    Supprime un conditionnement de la base de données par son ID.
    """
    conditionnement = db.query(Conditionnement).filter(Conditionnement.idcondit == idcondit).first()
    if not conditionnement:
        raise HTTPException(status_code=404, detail="Conditionnement non trouvé")

    db.delete(conditionnement)
    db.commit()
    return conditionnement
