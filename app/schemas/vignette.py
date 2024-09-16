from pydantic import BaseModel
from decimal import Decimal

class VignetteBase(BaseModel):
    valmin: Decimal
    valtimbre: Decimal

class VignetteCreate(VignetteBase):
    pass

class VignetteResponse(VignetteBase):
    id: int

    class Config:
        from_attributes = True
