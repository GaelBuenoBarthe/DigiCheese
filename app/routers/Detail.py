from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud
from app.schemas.detail import Detail, DetailCreate
from app.database import SessionLocal, get_db

router = APIRouter()



@router.post("/details/", response_model=Detail)
def create_detail(detail: DetailCreate, db: Session = Depends(get_db)):
    return crud.create_detail(db=db, detail=detail)

@router.get("/details/{id}", response_model=Detail)
def read_detail(id: int, db: Session = Depends(get_db)):
    db_detail = crud.get_detail(db, id=id)
    if db_detail is None:
        raise HTTPException(status_code=404, detail="Detail non trouvé")
    return db_detail

@router.get("/details/", response_model=List[Detail])
def read_details(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_details(db, skip=skip, limit=limit)

@router.put("/details/{id}", response_model=Detail)
def update_detail(id: int, detail: DetailCreate, db: Session = Depends(get_db)):
    return crud.update_detail(db=db, id=id, detail=detail)

@router.delete("/details/{id}", response_model=Detail)
def delete_detail(id: int, db: Session = Depends(get_db)):
    return crud.delete_detail(db=db, id=id)