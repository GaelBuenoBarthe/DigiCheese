from pydantic import BaseModel
from typing import Optional
from datetime import date

#Création d'une classe CommandeBase qui hérite de BaseModel
class CommandeBase(BaseModel):
    datcde: date
    codcli: int
    timbrecli: float
    timbre_cde: float
    nbcolis: Optional[int] = 1
    cheqcli: float
    idcondit: Optional[int] = 0
    cdeComt: Optional[str] = None
    barchive: Optional[int] = 0
    bstock: Optional[int] = 0

class CommandeCreate(CommandeBase):
    pass

class Commande(CommandeBase):
    codcde: int

    class Config:
        from_attributes = True