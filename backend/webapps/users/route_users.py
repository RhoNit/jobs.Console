from db.repository.users import create_new_user
from db.session import get_db

from schemas.users import UserCreate

from webapps.users.forms import UserCreateForm

from fastapi import APIRouter, Depends, Request, responses, status
from fastapi.templating import Jinja2Templates

from sqlalchemy.exc import IntegrityError
import sqlalchemy.orm as _orm


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/register")
def register(request: Request):
    return templates.TemplateResponse("users/register.html", {"request": request})


@router.post("/register")
async def register(request: Request, db: _orm.Session = Depends(get_db)):
    form = UserCreateForm(request)
    await form.load_data()
    if await form.is_valid():
        user = UserCreate(
            username=form.username, 
            email=form.email, 
            password=form.password
        )
        try:
            user = create_new_user(user=user, db=db)
            return responses.RedirectResponse("/?msg=Successfully-Registered", status_code=status.HTTP_302_FOUND)  # default is post request, to use get request added status code 302
        except IntegrityError:
            form.__dict__.get("errors").append("Duplicate username or email")
            return templates.TemplateResponse("users/register.html", form.__dict__)
            
    return templates.TemplateResponse("users/register.html", form.__dict__)
