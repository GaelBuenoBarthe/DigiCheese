from pydantic import BaseModel
from typing import Optional

class UtilisateurBase(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    # Add other fields as needed

class UtilisateurCreate(UtilisateurBase):
    name: str
    email: str

class UtilisateurUpdate(UtilisateurBase):
    pass

class UtilisateurResponse(UtilisateurBase):
    code_utilisateur: int

    class Config:
        orm_mode = True
