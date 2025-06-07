from sqlmodel import SQLModel, Field, Relationship
from typing import List
from pydantic import EmailStr
from datetime import datetime

class UserBase(SQLModel):
    username: str = Field(unique=True)
    email: EmailStr = Field(unique=True)

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: EmailStr = Field(unique=True, index=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    todo_lists: List["TodoList"] = Relationship(back_populates="owner")