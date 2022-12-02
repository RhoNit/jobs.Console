from db.models.jobs import Job
from schemas.jobs import JobCreate
import sqlalchemy.orm as _orm


def create_new_job(job: JobCreate, db: _orm.Session, owner_id: int):
    job_object = Job(**job.dict(), owner_id=owner_id)
    db.add(job_object)
    db.commit()
    db.refresh(job_object)

    return job_object


def get_job_by_id(id: int, db: _orm.Session):
    job_obj = db.query(Job).filter(Job.id == id).first()
    return job_obj


def get_all_jobs(db: _orm.Session):
    jobs = db.query(Job).all()
    return jobs


def update_job_by_id(id: int, job: JobCreate, db: _orm.Session, owner_id):
    existing_job = db.query(Job).filter(Job.id == id)
    if not existing_job.first():
        return 0
    
    job.__dict__.update(owner_id=owner_id)  # update dictionary with new key value of owner_id
    existing_job.update(job.__dict__)
    db.commit()
    return 1


def delete_job_by_id(id: int, db: _orm.Session, owner_id):
    existing_job = db.query(Job).filter(Job.id == id)
    if not existing_job.first():
        return 0
    existing_job.delete(synchronize_session=False)
    db.commit()
    return 1


def search_job(query: str, db: _orm.Session):
    jobs = db.query(Job).filter(Job.title.contains(query))
    return jobs
