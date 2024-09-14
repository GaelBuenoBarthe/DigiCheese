from pydantic import BaseModel
from typing import Optional

class DetailBase(BaseModel):
    codcde: int
    qte: Optional[int] = 1
    colis: Optional[int] = 1
    commentaire: Optional[str] = None

class DetailCreate(DetailBase):
    pass

class Detail(DetailBase):
    id: int

    class Config:
        from_attributes = True