from typing import Optional, List

from apis.v1.route_login import get_current_user_from_token

from db.models.users import User
from db.repository.jobs import create_new_job, get_job_by_id, get_all_jobs, update_job_by_id, delete_job_by_id, search_job
from db.session import get_db

from schemas.jobs import JobCreate, ShowJob

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.templating import Jinja2Templates

import sqlalchemy.orm as _orm


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.post("/create-job", response_model=ShowJob)
def create_job(job: JobCreate, db: _orm.Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    job_obj = create_new_job(job=job, db=db, owner_id=current_user.id)
    return job_obj


@router.get("/get/{id}", response_model=ShowJob)
def read_job(id: int, db: _orm.Session = Depends(get_db)):
    job_obj = get_job_by_id(id=id, db=db)
    if not job_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job associated with ID '{id}' does not exist")

    return job_obj


@router.get("/all", response_model=List[ShowJob])
def read_jobs(db: _orm.Session = Depends(get_db)):
    jobs = get_all_jobs(db=db)
    return jobs


@router.put("/update/{id}")
def update_job(id: int, job: JobCreate, db: _orm.Session = Depends(get_db)):
    current_user = 1
    message = update_job_by_id(id=id, job=job, db=db, owner_id=current_user)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job associated with ID '{id}' not found")

    return {"msg": "Successfully updated data."}


@router.delete("/delete/{id}")
def delete_job(id: int, db: _orm.Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    job_obj = get_job_by_id(id=id, db=db)
    if not job_obj:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job associated with ID '{id}' does not exist")
    
    print(job_obj.owner_id, current_user.id, current_user.is_superuser)
    
    if job_obj.owner_id == current_user.id or current_user.is_superuser:
        delete_job_by_id(id=id, db=db, owner_id=current_user.id)
        return {"detail": "Successfully deleted"}

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not permitted")


@router.get("/autocomplete")
def autocomplete(term: Optional[str] = None, db: _orm.Session = Depends(get_db)):
    jobs = search_job(term, db=db)
    job_titles = []
    for job in jobs:
        job_titles.append(job.title)
    return job_titles
