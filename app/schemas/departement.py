from pydantic import BaseModel
from typing import List

class DepartementBase(BaseModel):
    code: str
    nom: str

class DepartementCreate(DepartementBase):
    pass

class DepartementUpdate(DepartementBase):
    pass

class Departement(DepartementBase):
    id: int
    communes: List['Commune'] = []

    class Config:
        orm_mode = True