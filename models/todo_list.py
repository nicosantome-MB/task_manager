from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime

class TodoList(SQLModel, table=True):
    __tablename__ = "todo_list"
    id: int = Field(default=None, primary_key=True)
    username: str 
    description: Optional[str]
    owner_id: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    owner: "User" = Relationship(back_populates="todo_lists")
    tasks: List["Task"] = Relationship(back_populates="todo_list")