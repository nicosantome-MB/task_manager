from sqlmodel import Session, select
from models.task import Task
from typing import Optional


# POST
def create_task(session: Session, task: Task):
    existing_task = session.exec(select(Task).where(Task.title == task.title)).first()
    if existing_task:
        raise ValueError(f"A task with title '{task.title}' already exists.")
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


# GET
def get_all_tasks(session: Session, offset: int = 0, limit: Optional[int] = None):
    query = select(Task).offset(offset)  
    if limit is not None:
        query = query.limit(limit)  
    return session.exec(query).all()

def get_task_by_id(session: Session, task_id: int):
    return session.get(Task, task_id)

def get_tasks_by_todo_list(session: Session, todo_id: int):
    return session.exec(select(Task).where(Task.todo_list_id == todo_id)).all()

def get_tasks_by_status(session: Session, status: bool):
    return session.exec(select(Task).where(Task.status == status)).all()

