from db.base_class import Base

import sqlalchemy as _sql
import sqlalchemy.orm as _orm


class User(Base):
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    username = _sql.Column(_sql.String, unique=True, nullable=False)
    email = _sql.Column(_sql.String, nullable=False, unique=True, index=True)
    hashed_password = _sql.Column(_sql.String, nullable=False)
    is_active = _sql.Column(_sql.Boolean(), default=True)
    is_superuser = _sql.Column(_sql.Boolean(), default=False)
    
    jobs = _orm.relationship("Job", back_populates="owner")
