from typing import Generator

from configurator.config import settings

import sqlalchemy as _sql
import sqlalchemy.orm as _orm


# for sqlite
if settings.USE_SQLITE_DB == "True":
	SQLALCHEMY_DATABASE_URL = "sqlite:///./datastore.db"
	engine = _sql.create_engine(
		SQLALCHEMY_DATABASE_URL, 
		connect_args={"check_same_thread": False}
	)
	
# for other production DBs
else:
	SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
	engine = _sql.create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
