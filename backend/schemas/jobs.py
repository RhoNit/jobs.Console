from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class JobBase(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    link: Optional[str] = None
    location: Optional[str] = "Remote"
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()


# this will be used to validate data while creating a Job
class JobCreate(JobBase):
    title: str
    company: str
    location: str
    description: str

        
class ShowJob(JobBase):
    title: str
    company: str
    link: Optional[str]
    location: str
    date_posted: date
    description: Optional[str]

    class Config:
        orm_mode = True
