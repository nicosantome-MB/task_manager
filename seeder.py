from sqlmodel import SQLModel, Session
from db.database import engine, create_db_and_tables, drop_db_and_tables
from models.user import User
from models.task import Task
from models.todo_list import TodoList
from models.task_status import TaskStatus

def seed_data():
    # Borrar la base de datos y las tablas existentes
    drop_db_and_tables() 
    # Crear la base de datos y las tablas
    create_db_and_tables()

    with Session(engine) as session:
        # Crear autores
        try:
            user1 = User(username="user1", email="user1@example.com", hashed_password="hashed_password1")
            user2 = User(username="user2", email="user2@example.com", hashed_password="hashed_password2")
            session.add_all([user1, user2])
            session.commit()
        except Exception as e:
            print(f"Error creating users: {e}")

        # Create todo_lists
        try:
            todo_list1 = TodoList(username="user1", description="Todo List 1", owner_id=user1.id)
            todo_list2 = TodoList(username="user2", description="Todo List 2", owner_id=user2.id)
            session.add_all([todo_list1, todo_list2])
            session.commit()
        except Exception as e:
            print(f"Error creating todo lists: {e}")

          # Crear estados de tareas
        try:
            status1 = TaskStatus(name="Pending", color="red")
            status2 = TaskStatus(name="Completed", color="green")
            session.add_all([status1, status2])
            session.commit()
        except Exception as e:
            print(f"Error creating task statuses: {e}")

        # Crear tareas
        try:
            task1 = Task(title="Task 1", description="Description for task 1", todo_list_id=todo_list1.id, status_id=status1.id)
            task2 = Task(title="Task 2", description="Description for task 2", todo_list_id=todo_list2.id, status_id=status2.id)
            session.add_all([task1, task2])
            session.commit()
            print("Tasks created")
        except Exception as e:
            print(f"Error creating tasks: {e}")

if __name__ == "__main__":
    seed_data()
