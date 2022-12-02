from db.base_class import Base

import sqlalchemy as _sql
import sqlalchemy.orm as _orm


class Job(Base):
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    title = _sql.Column(_sql.String, nullable=False)
    company = _sql.Column(_sql.String, nullable=False)
    link = _sql.Column(_sql.String)
    location = _sql.Column(_sql.String, nullable=False)
    description = _sql.Column(_sql.String, nullable=False)
    date_posted = _sql.Column(_sql.Date)
    is_active = _sql.Column(_sql.Boolean(), default=True)
    owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("user.id"))
    
    owner = _orm.relationship("User", back_populates="jobs")
