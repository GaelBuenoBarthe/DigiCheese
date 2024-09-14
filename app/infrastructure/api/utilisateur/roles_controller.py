from fastapi import  HTTPException
from sqlalchemy.orm import Session
from app.models.utilisateur import role
from app.schemas.role import RoleCreate, RoleResponse



@router.get("/", response_model=list[RoleResponse])
def get_roles(db: Session, skip: int = 0, limit: int = 10 ):
    roles = db.query(role).offset(skip).limit(limit).all()
    return roles

@router.post("/", response_model=RoleResponse)
def create_role(role_data: RoleCreate, db: Session):
    db_role = role(**role_data.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

@router.get("/{role_id}", response_model=RoleResponse)
def get_role(role_id: int, db: Session):
    db_role = db.query(role).filter(role.id == role_id).first()
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.delete("/{role_id}", response_model=RoleResponse)
def delete_role(role_id: int, db: Session):
    db_role = db.query(role).filter(role.id == role_id).first()
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    db.delete(db_role)
    db.commit()
    return db_role