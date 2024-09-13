from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models
from .database import SessionLocal, engine
from routers import (roles, utilisateurs)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Include routers
app.include_router(utilisateur_router, prefix="/utilisateurs", tags=["Utilisateurs"])
app.include_router(role_router, prefix="/roles", tags=["Roles"])
@app.get("/")
def read_root():
    return {"Bienvenue dans Digicheese !"}

@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Et non !!! c'est raté")
    return item