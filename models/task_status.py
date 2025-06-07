from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class TaskStatus(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    color: Optional[str]
    tasks: List["Task"] = Relationship(back_populates="status")