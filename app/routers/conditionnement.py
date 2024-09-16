from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.conditionnement import Conditionnement  # Assuming you have this path for your models
from app.schemas.conditionnement import ConditionnementCreate, ConditionnementResponse  # Pydantic schemas

router = APIRouter()

# Route pour récupérer tous les conditionnements avec pagination
@router.get("/", response_model=list[ConditionnementResponse])
def get_conditionnements(db: Session, skip: int = 0, limit: int = 10):
    """
    Récupérer tous les conditionnements avec un skip/limit pour la pagination.
    """
    conditionnements = db.query(Conditionnement).offset(skip).limit(limit).all()
    return conditionnements

# Route pour créer un nouveau conditionnement
@router.post("/", response_model=ConditionnementResponse)
def create_conditionnement(conditionnement: ConditionnementCreate, db: Session):
    """
    Créer un nouveau conditionnement et l'ajouter à la base de données.
    """
    db_conditionnement = Conditionnement(**conditionnement.dict())
    db.add(db_conditionnement)
    db.commit()
    db.refresh(db_conditionnement)
    return db_conditionnement

# Route pour récupérer un conditionnement par son ID
@router.get("/{idcondit}", response_model=ConditionnementResponse)
def get_conditionnement(idcondit: int, db: Session):
    """
    Récupérer un conditionnement spécifique par son ID.
    """
    conditionnement = db.query(Conditionnement).filter(Conditionnement.idcondit == idcondit).first()
    if not conditionnement:
        raise HTTPException(status_code=404, detail="Conditionnement non trouvé")
    return conditionnement

# Route pour mettre à jour un conditionnement existant
@router.put("/{idcondit}", response_model=ConditionnementResponse)
def update_conditionnement(idcondit: int, conditionnement_update: ConditionnementCreate, db: Session):
    """
    Mettre à jour les informations d'un conditionnement existant par son ID.
    """
    conditionnement = db.query(Conditionnement).filter(Conditionnement.idcondit == idcondit).first()
    if not conditionnement:
        raise HTTPException(status_code=404, detail="Conditionnement non trouvé")

    for key, value in conditionnement_update.dict(exclude_unset=True).items():
        setattr(conditionnement, key, value)

    db.commit()
    db.refresh(conditionnement)
    return conditionnement

# Route pour supprimer un conditionnement par son ID
@router.delete("/{idcondit}", response_model=ConditionnementResponse)
def delete_conditionnement(idcondit: int, db: Session):
    """
    Supprimer un conditionnement spécifique par son ID.
    """
    conditionnement = db.query(Conditionnement).filter(Conditionnement.idcondit == idcondit).first()
    if not conditionnement:
        raise HTTPException(status_code=404, detail="Conditionnement non trouvé")

    db.delete(conditionnement)
    db.commit()
    return conditionnement
