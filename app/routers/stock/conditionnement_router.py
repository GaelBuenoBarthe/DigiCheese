# app/routers/conditionnement_router.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.stock.conditionnements import ConditionnementCreate, ConditionnementResponse
from app.infrastructure.api.stock.conditionnements_controller import (
    get_conditionnements as get_conditionnements_ctrl,
    create_conditionnement as create_conditionnement_ctrl,
    get_conditionnement_by_id as get_conditionnement_ctrl,
    update_conditionnement as update_conditionnement_ctrl,
    delete_conditionnement as delete_conditionnement_ctrl
)
from app.database import get_db  # Assuming you have a get_db function for session

router = APIRouter()

# Route to get all conditionnements
@router.get("/", response_model=list[ConditionnementResponse])
def get_conditionnements_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_conditionnements_ctrl(db=db, skip=skip, limit=limit)

# Route to create a new conditionnement
@router.post("/", response_model=ConditionnementResponse)
def create_conditionnement_route(conditionnement: ConditionnementCreate, db: Session = Depends(get_db)):
    return create_conditionnement_ctrl(conditionnement=conditionnement, db=db)

# Route to get a conditionnement by ID
@router.get("/{idcondit}", response_model=ConditionnementResponse)
def get_conditionnement_route(idcondit: int, db: Session = Depends(get_db)):
    return get_conditionnement_ctrl(idcondit=idcondit, db=db)

# Route to update a conditionnement
@router.put("/{idcondit}", response_model=ConditionnementResponse)
def update_conditionnement_route(idcondit: int, conditionnement_update: ConditionnementCreate, db: Session = Depends(get_db)):
    return update_conditionnement_ctrl(idcondit=idcondit, conditionnement_update=conditionnement_update, db=db)

# Route to delete a conditionnement
@router.delete("/{idcondit}", response_model=ConditionnementResponse)
def delete_conditionnement_route(idcondit: int, db: Session = Depends(get_db)):
    return delete_conditionnement_ctrl(idcondit=idcondit, db=db)
