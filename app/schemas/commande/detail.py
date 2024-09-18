from pydantic import BaseModel
from typing import Optional
from datetime import date



#Création d'une classe CommandeBase qui hérite de BaseModel
class DetailBase(BaseModel):
    detail_id: int
    objet_id: int
    name: str

class DetailCreate(DetailBase):
    pass

class Detail(DetailBase):
    codcde: int

    class Config:
        from_attributes = True