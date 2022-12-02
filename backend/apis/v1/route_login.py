from datetime import timedelta

from apis.utils import OAuth2PasswordBearerWithCookie

from configurator.config import settings
from configurator.hashing import Hasher
from configurator.security import create_access_token

from db.repository.login import get_user
from db.session import get_db

from schemas.tokens import Token

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm

from jose import jwt
from jose import JWTError

import sqlalchemy.orm as _orm


router = APIRouter()


def authenticate_user(username: str, password: str, db: _orm.Session = Depends(get_db)):
    user_obj = get_user(username=username, db=db)
    
    print(user_obj)
    
    if not user_obj:
        return False
    if not Hasher.verify_password(password, user_obj.hashed_password):
        return False

    return user_obj


@router.post("/token", response_model=Token)
def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends(), db: _orm.Session = Depends(get_db)):
    user_obj = authenticate_user(form_data.username, form_data.password, db)
    if not user_obj:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user_obj.email}, 
        expires_delta=access_token_expires
    )
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)

    return {"access_token": access_token, "token_type": "bearer"}


oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/login/token")


def get_current_user_from_token(token: str = Depends(oauth2_scheme), db: _orm.Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials"
    )
    try:
        payload = jwt.decode(
            token, 
            settings.SECRET_KEY, 
            algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        print("username/email extracted is ", username)
        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception
    user_obj = get_user(username=username, db=db)
    if user_obj is None:
        raise credentials_exception
        
    return user_obj
