from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import date

class UtilisateurBase(BaseModel):
    nom_utilisateur: Optional[str] = None
    prenom_utilisateur: Optional[str] = None
    username: Optional[str] = None
    couleur_fond_utilisateur: Optional[int] = 0
    date_insc_utilisateur: Optional[date] = None

class UtilisateurCreate(UtilisateurBase):
    pass

class UtilisateurResponse(UtilisateurBase):
    code_utilisateur: int

    class Config:
        orm_mode = True

class UtilisateurUpdate(BaseModel):
    nom_utilisateur: Optional[str] = None
    prenom_utilisateur: Optional[str] = None
    username: Optional[str] = None
    couleur_fond_utilisateur: Optional[int] = 0
    date_insc_utilisateur: Optional[date] = None

    class Config:
        orm_mode = True