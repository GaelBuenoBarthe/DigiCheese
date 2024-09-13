from pydantic import BaseModel
from typing import List, Optional

class ClientBase(BaseModel):
    genre: Optional[str]
    nom: str
    prenom: str
    adresse1: str
    adresse2: Optional[str]
    adresse3: Optional[str]
    ville_id: int
    telephone: Optional[str]
    email: Optional[str]
    portable: Optional[str]
    newsletter: Optional[bool]

class ClientCreate(ClientBase):
    pass

class ClientUpdate(ClientBase):
    pass

class Client(ClientBase):
    id: int
    commandes: List['Commande'] = []

    class Config:
        orm_mode = True