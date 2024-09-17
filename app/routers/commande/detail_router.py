from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.commandes.detail import Detail, DetailCreate
from app.database import get_db
from app.infrastructure.api.commande.details_controller import (
    create_detail,
    get_detail,
    get_details,
    update_detail,
    delete_detail
)

router = APIRouter()

@router.post("/details/", response_model=Detail)
def create_detail_route(detail: DetailCreate, db: Session = Depends(get_db)):
    return create_detail(db=db, detail=detail)

@router.get("/details/{id}", response_model=Detail)
def read_detail_route(id: int, db: Session = Depends(get_db)):
    db_detail = get_detail(db, id=id)
    if not db_detail:
        raise HTTPException(status_code=404, detail="Detail non trouvé")
    return db_detail

@router.get("/details/", response_model=List[Detail])
def read_details_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_details(db, skip=skip, limit=limit)

@router.put("/details/{id}", response_model=Detail)
def update_detail_route(id: int, detail: DetailCreate, db: Session = Depends(get_db)):
    db_detail = update_detail(db=db, id=id, detail=detail)
    if not db_detail:
        raise HTTPException(status_code=404, detail="Detail non trouvé")
    return db_detail

@router.delete("/details/{id}", response_model=Detail)
def delete_detail_route(id: int, db: Session = Depends(get_db)):
    db_detail = delete_detail(db=db, id=id)
    if not db_detail:
        raise HTTPException(status_code=404, detail="Detail non trouvé")
    return db_detail
