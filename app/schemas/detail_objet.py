from pydantic import BaseModel
from typing import Optional

# Base class for creating and updating DetailObjet
class DetailObjetBase(BaseModel):
    codcde: int
    qte: Optional[int] = 1
    colis: Optional[int] = 1
    commentaire: Optional[str] = None

# For creating a new DetailObjet (inherits from base)
class DetailObjetCreate(DetailObjetBase):
    pass

# For representing the response (includes id and possibly more attributes)
class DetailObjetResponse(DetailObjetBase):
    id: int  # Unique identifier for the DetailObjet

    class Config:
        from_attributes = True  # Allows Pydantic to work with SQLAlchemy models
