from configurator.hashing import Hasher
from db.models.users import User
from schemas.users import UserCreate

import sqlalchemy.orm as _orm


def create_new_user(user: UserCreate, db: _orm.Session):
    user_obj = User(
        username=user.username,
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj


def get_user_by_email(email: str, db: _orm.Session):
    user_obj = db.query(User).filter(User.email == email).first()
    return user_obj
