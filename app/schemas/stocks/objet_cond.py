from pydantic import BaseModel
from typing import Optional

# Base Schema for ObjetCond
class ObjetCondBase(BaseModel):
    qteobjdeb: int
    qteobjfin: int
    codobj: int  # ForeignKey reference to Objet
    codcond: int  # ForeignKey reference to Conditionnement

# Create Schema for ObjetCond (no id required here)
class ObjetCondCreate(ObjetCondBase):
    pass

# Response Schema for ObjetCond (includes id)
class ObjetCondResponse(ObjetCondBase):
    idrelcond: int

    class Config:
        from_attributes = True
