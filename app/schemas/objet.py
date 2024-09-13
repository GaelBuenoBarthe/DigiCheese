from pydantic import BaseModel
from typing import Optional

# Schéma pour la création d'un objet
class ObjetCreate(BaseModel):
    libobj: Optional[str]
    tailleobj: Optional[str]
    puobj: Optional[float]
    poidsobj: Optional[float]
    indispobj: Optional[int]
    o_imp: Optional[int]
    o_aff: Optional[int]
    o_cartp: Optional[int]
    points: Optional[int]
    o_ordre_aff: Optional[int]

    class Config:
        orm_mode = True

# Schéma pour lire un objet (y compris l'identifiant)
class Objet(BaseModel):
    codobj: int
    libobj: Optional[str]
    tailleobj: Optional[str]
    puobj: Optional[float]
    poidsobj: Optional[float]
    indispobj: Optional[int]
    o_imp: Optional[int]
    o_aff: Optional[int]
    o_cartp: Optional[int]
    points: Optional[int]
    o_ordre_aff: Optional[int]

    class Config:
        orm_mode = True
