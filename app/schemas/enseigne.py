from pydantic import BaseModel

class EnseigneBase(BaseModel):
    """
    Schéma de base pour une enseigne.
    """
    libelle: str
    ville: str
    departement_id: int

class EnseigneCreate(EnseigneBase):
    """
    Schéma pour la création d'une nouvelle enseigne.
    """
    pass

class EnseigneUpdate(EnseigneBase):
    """
    Schéma pour la mise à jour d'une enseigne existante.
    """
    pass

class EnseigneResponse(EnseigneBase):
    """
    Schéma de réponse pour une enseigne, incluant l'ID.
    """
    id: int

    class Config:
        orm_mode = True
