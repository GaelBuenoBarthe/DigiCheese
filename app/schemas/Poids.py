from pydantic import BaseModel
from decimal import Decimal

class PoidsBase(BaseModel):
    valmin: Decimal
    valtimbre: Decimal

class PoidsCreate(PoidsBase):
    pass

class PoidsResponse(PoidsBase):
    id: int

    class Config:
        orm_mode = True
