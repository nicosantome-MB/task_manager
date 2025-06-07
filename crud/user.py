from sqlmodel import Session, select
from models.user import User
from main import logger

# POST
def create_user(session: Session, user: User):
    try:
        existing_user = session.exec(select(User).where(User.email == user.email)).first()
        if existing_user:
            logger.error(f"A user with email '{user.email}' already exists.")
            raise ValueError(f"A user with email '{user.email}' already exists.")
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        logger.exception(f"Error creating user: {e}")
        raise

# GET
def get_users(session: Session):
    return session.exec(select(User)).all()

def get_user_by_id(session: Session, user_id: int):
    return session.get(User, user_id)

def get_user_by_email(session: Session, email: str):
    return session.exec(select(User).where(User.email == email))

def get_user_by_username(session: Session, username: str):
    return session.exec(select(User).where(User.username == username))


# PUT
def update_user(session: Session, user_id: int, user_data: dict):
    user = session.get(User, user_id)
    if not user:
        return None
    for key, value in user_data.items():
        setattr(user, key, value)
    session.commit()
    session.refresh(user)
    return user


# DELETE
def delete_user(session: Session, user_id: int):
    user = session.get(User, user_id)
    if user:
        session.delete(user)
        session.commit()
        return user
    