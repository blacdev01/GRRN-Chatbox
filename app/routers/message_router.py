from fastapi import APIRouter, Depends
from typing import List, Optional
from app.schemas.message_schemas import MessageIn, MessageOut
from app.models.message_models import Message
from app.DB.connection import get_db
from sqlalchemy.orm import Session


router = APIRouter()



@router.get("/messages/{receiver_id}", response_model=List[MessageOut])
async def get_messages(receiver_id: int, sender_id: Optional[int] = None, db: Session = Depends(get_db)):

    if sender_id:
        messages = db.query(Message).filter(
            ((Message.sender_id == sender_id) & (Message.receiver_id == receiver_id)) |
            ((Message.sender_id == receiver_id) & (Message.receiver_id == sender_id))
        ).all()
    else:
        messages = db.query(Message).filter(Message.receiver_id == receiver_id).all()
    db.close()
    return messages


@router.post("/messages", response_model=MessageOut)
async def send_message(message: MessageIn, db: Session = Depends(get_db)):
    db_message = Message(**message.model_dump())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    db.close()
    return db_message