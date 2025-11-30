from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class UserBase(BaseModel):
    email: str
    name: Optional[str] = None
    consent_given: bool = False

class UserCreate(UserBase):
    pass

class ConversationBase(BaseModel):
    user_id: UUID
    status: str = "active"

class MessageBase(BaseModel):
    content: str
    role: str

class MessageCreate(MessageBase):
    conversation_id: UUID
