from pydantic import BaseModel
from typing import Optional

#Création d'une classe DetailObjetBase qui hérite de BaseModel
class DetailObjetBase(BaseModel):
    codcde: int
    qte: Optional[int] = 1
    colis: Optional[int] = 1
    commentaire: Optional[str] = None

class DetailObjetCreate(DetailObjetBase):
    pass

class DetailObjet(DetailObjetBase):
    id: int

    class Config:
        from_attributes = True