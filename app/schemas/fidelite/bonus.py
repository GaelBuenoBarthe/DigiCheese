from pydantic import BaseModel

class Bonus(BaseModel):
    id: int
    description: str
    points: float

    class Config:
        orm_mode = True