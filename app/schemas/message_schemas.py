from pydantic import BaseModel



class MessageIn(BaseModel):
    sender_id: int
    receiver_id: int
    content: str

class MessageOut(MessageIn):
    id: int