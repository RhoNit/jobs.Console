
from fastapi import APIRouter, Depends

import sqlalchemy.orm as _orm

from db.repository.users import create_new_user
from db.session import get_db

from schemas.users import UserCreate, ShowUser


router = APIRouter()


@router.post("/", response_model=ShowUser)
def create_user(user: UserCreate, db: _orm.Session = Depends(get_db)):
    user_obj = create_new_user(user=user, db=db)
    return user_obj
