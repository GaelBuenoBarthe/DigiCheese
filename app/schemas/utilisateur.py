from typing import Optional
from pydantic import BaseModel

class UtilisateurBase(BaseModel):
    name: str
    email: str

class UtilisateurCreate(UtilisateurBase):
    password: str

class UtilisateurResponse(UtilisateurBase):
    id: int

class UtilisateurUpdate(BaseModel):
    nom: Optional[str] = None
    email: Optional[str] = None

    class Config:
        orm_mode = True