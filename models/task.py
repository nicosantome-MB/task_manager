from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime, date
from todo_list import TodoList

class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(...)
    description: Optional[str]
    due_date: Optional[date]
    is_completed: bool = Field(default=False)
    todo_list_id: int = Field(foreign_key="todo_list.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Usar strings para las relaciones
    todo_list: Optional["TodoList"] = Relationship(back_populates="tasks")
    status: Optional["TaskStatus"] = Relationship(back_populates="tasks")

# Elimina cualquier importación diferida o __init__ personalizado