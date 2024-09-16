from typing import Optional
from pydantic import BaseModel, Field
from decimal import Decimal

class ConditionnementCreate(BaseModel):
    libcondit: str = Field(..., max_length=50)  # Name of the conditionnement, required
    poidscondit: int  # Weight of the conditionnement, required
    prixcond: Decimal = Field(..., gt=0)  # Price of the conditionnement, required, must be greater than 0
    ordreimp: int  # Order of importance

    class Config:
        from_attributes = True  # Enable ORM mode to support SQLAlchemy models

class ConditionnementResponse(BaseModel):
    idcondit: int  # ID of the conditionnement
    libcondit: str  # Name of the conditionnement
    poidscondit: int  # Weight of the conditionnement
    prixcond: Decimal  # Price of the conditionnement
    ordreimp: int  # Order of importance

    class Config:
        from_attributes = True  # Enable ORM mode to support SQLAlchemy models

class ConditionnementUpdate(BaseModel):
    libcondit: Optional[str] = Field(None, max_length=50)  # Optional name of the conditionnement
    poidscondit: Optional[int]  # Optional weight of the conditionnement
    prixcond: Optional[Decimal] = Field(None, gt=0)  # Optional price of the conditionnement
    ordreimp: Optional[int]  # Optional order of importance

    class Config:
        from_attributes = True  # Enable ORM mode to support SQLAlchemy models