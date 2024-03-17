from typing import List
from app.models.user_models import User
from app.DB.connection import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.schemas.user_schemas import UserOut


router = APIRouter()

@router.get("/users/", response_model=List[UserOut])
async def get_users(db: Session = Depends(get_db)):

    users = db.query(User).all()
    db.close()
    return users



# def add_2_default_users(db: Session):
#     user1 = User(username="user1")
#     user2 = User(username="user2")
#     db.add(user1)
#     db.add(user2)
#     db.commit()
#     db.refresh(user1)
#     db.refresh(user2)
#     db.close()
#     return user1, user2

# add_2_default_users(next(get_db()))