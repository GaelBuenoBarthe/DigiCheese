from sqlalchemy.orm import Session
from . import models

def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()