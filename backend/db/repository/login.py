from db.models.users import User
import sqlalchemy.orm as _orm


def get_user(username: str, db: _orm.Session):
    user_obj = db.query(User).filter(User.email == username).first()
    return user_obj
