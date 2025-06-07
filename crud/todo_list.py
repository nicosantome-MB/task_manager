from typing import Optional
from sqlmodel import Session, select
from models.todo_list import TodoList

# POST
def create_list(session: Session, list: TodoList):
    existing_list = session.exec(select(TodoList).where(TodoList.name == list.name)) # Ver esto
    if existing_list:
        raise ValueError(f"A list named '{list.name}' already exists.")
    session.add(list)
    session.commit()
    session.refresh(list)


# GET
def get_lists(session: Session, skip: Optional[int] = 0, limit: Optional[int] = 100):
    query = select(TodoList).offset(skip).limit(limit)
    return session.exec(query).all()

def get_list_by_id(session: Session, list_id: int):
    return session.get(TodoList, list_id)

def get_list_by_owner_id(session: Session, owner_id: int):
    return session.exec(select(TodoList).where(TodoList.owner_id == owner_id))

def get_list_by_username(session: Session, username: str):
    return session.exec(select(TodoList).where(TodoList.username == username)) 


# PUT
def update_list(session: Session, list_id: int, list_data: dict):
    list = session.get(TodoList, list_id)
    if not list:
        return None
    for key, value in list_data.items():
        setattr(list, key, value)
    session.commit()
    session.refresh(list)
    return list


# DELETE
def delete_list(session: Session, list_id: int):
    list = session.get(TodoList, list_id)
    if list:
        session.delete(list)
        session.commit()
        return list