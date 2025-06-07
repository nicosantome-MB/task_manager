from sqlmodel import Session, select
from models.task_status import TaskStatus
from typing import Optional

def create_task_status(session: Session, name: str, color: Optional[str] = None):
    task_status = TaskStatus(name=name, color=color)
    session.add(task_status)
    session.commit()
    session.refresh(task_status)
    return task_status

def get_task_status(session: Session, status_id: int):
    return session.get(TaskStatus, status_id)

def get_all_task_status(session: Session):
    return session.exec(select(TaskStatus)).all()

def update_task_status(session: Session, status_id: int, name: str, color: Optional[str] = None):
    task_status = session.get(TaskStatus, status_id)
    if task_status:
        task_status.name = name
        task_status.color = color
        session.commit()
        session.refresh(task_status)
    return task_status

def delete_task_status(session: Session, status_id: int):
    task_status = session.get(TaskStatus, status_id)
    if task_status:
        session.delete(task_status)
        session.commit()
    return task_status