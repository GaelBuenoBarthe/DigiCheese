from pydantic import BaseModel, EmailStr
from typing import Optional

class ClientBase(BaseModel):
    genre: Optional[str] = None
    nom: str
    prenom: Optional[str] = None
    adresse1: Optional[str] = None
    adresse2: Optional[str] = None
    adresse3: Optional[str] = None
    ville_id: Optional[int] = None
    telephone: Optional[str] = None
    email: Optional[EmailStr] = None
    portable: Optional[str] = None
    newsletter: Optional[bool] = None

class ClientCreate(ClientBase):
    pass

class ClientUpdate(ClientBase):
    pass

class ClientResponse(BaseModel):
    id: int
    genre: Optional[str] = None
    nom: str
    prenom: Optional[str] = None
    adresse1: Optional[str] = None
    adresse2: Optional[str] = None
    adresse3: Optional[str] = None
    ville_id: Optional[int] = None
    telephone: Optional[str] = None
    email: Optional[EmailStr] = None
    portable: Optional[str] = None
    newsletter: Optional[bool] = None

    class Config:
        orm_mode = True
