from pydantic import BaseModel

class ClientBase(BaseModel):
    """
    Schéma de base pour un client, contenant les attributs communs pour la création et la mise à jour.
    """
    genre: str
    nom: str
    prenom: str | None = None
    adresse1: str | None = None
    adresse2: str | None = None
    adresse3: str | None = None
    ville_id: int
    telephone: str | None = None
    email: str | None = None
    portable: str | None = None
    newsletter: bool | None = None

class ClientCreate(ClientBase):
    """
    Schéma pour la création d'un nouveau client. Tous les champs sont obligatoires, sauf ceux marqués comme optionnels dans ClientBase.
    """
    pass

class ClientUpdate(ClientBase):
    """
    Schéma pour la mise à jour d'un client existant. Tous les champs sont optionnels.
    """
    pass


class Client(ClientBase):
    """
    Schéma de réponse pour un client, incluant l'ID et potentiellement d'autres relations (comme les commandes).
    """
    id: int
    # commandes: list[Commande] = []  # Si vous voulez inclure les commandes du client dans la réponse

    class Config:
        orm_mode = True  # Permet de créer des instances de ce schéma à partir d'objets SQLAlchemy