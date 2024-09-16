from pydantic import BaseModel

class DepartementBase(BaseModel):
    """
    Schéma de base pour un département.
    """
    code: str
    nom: str

class DepartementCreate(DepartementBase):
    """
    Schéma pour la création d'un nouveau département.
    """
    pass

class DepartementUpdate(DepartementBase):
    """
    Schéma pour la mise à jour d'un département existant.
    """
    pass

class DepartementResponse(DepartementBase):
    """
    Schéma de réponse pour un département, incluant l'ID.
    """
    id: int

    class Config:
        from_attributes = True
