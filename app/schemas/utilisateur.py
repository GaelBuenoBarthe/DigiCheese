from typing import Optional

from pydantic import BaseModel, EmailStr


class UtilisateurBase(BaseModel):
    name: str
    email: str

class UtilisateurCreate(UtilisateurBase):
    password: str

class UtilisateurResponse(UtilisateurBase):
    id: int

    class Config:
        orm_mode = True

# Adding UtilisateurUpdate for partial updates
class UtilisateurUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

    class Config:
        orm_mode = True
