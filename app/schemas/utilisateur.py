from pydantic import BaseModel

class UtilisateurBase(BaseModel):
    name: str
    email: str

class UtilisateurCreate(UtilisateurBase):
    password: str

class UtilisateurResponse(UtilisateurBase):
    id: int

    class Config:
        orm_mode = True