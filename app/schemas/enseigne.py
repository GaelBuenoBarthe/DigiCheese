from pydantic import BaseModel

class EnseigneBase(BaseModel):
    libelle: str
    ville: str
    departement_id: int

class EnseigneCreate(EnseigneBase):
    pass

class EnseigneUpdate(EnseigneBase):
    pass

class Enseigne(EnseigneBase):
    id: int

    class Config:
        orm_mode = True