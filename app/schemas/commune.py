from pydantic import BaseModel
from typing import List

class CommuneBase(BaseModel):
    code_postal: str
    nom: str
    departement_id: int

class CommuneCreate(CommuneBase):
    pass

class CommuneUpdate(CommuneBase):
    pass

class Commune(CommuneBase):
    id: int
    clients: List['Client'] = []

    class Config:
        orm_mode = True