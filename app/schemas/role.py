from pydantic import BaseModel

class RoleBase(BaseModel):
    librole: str

class RoleCreate(RoleBase):
    pass

class RoleResponse(RoleBase):
    codrole: int

    class Config:
        orm_mode = True
