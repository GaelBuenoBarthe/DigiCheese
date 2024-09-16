from pydantic import BaseModel

class CommuneBase(BaseModel):
    """
    Schéma de base pour une commune.
    """
    code_postal: str
    nom: str
    departement_id: int

class CommuneCreate(CommuneBase):
    """
    Schéma pour la création d'une nouvelle commune.
    """
    pass

class CommuneUpdate(CommuneBase):
    """
    Schéma pour la mise à jour d'une commune existante.
    """
    pass

class CommuneResponse(CommuneBase):
    """
    Schéma de réponse pour une commune, incluant l'ID.
    """
    id: int

    class Config:
        orm_mode = True
