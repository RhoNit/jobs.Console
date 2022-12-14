import databases
from db.session import SQLALCHEMY_DATABASE_URL


async def check_db_connected():
    try:
        if not str(SQLALCHEMY_DATABASE_URL).__contains__("sqlite"):
            database = databases.Database(SQLALCHEMY_DATABASE_URL)
            if not database.is_connected:
                await database.connect()
                await database.execute("SELECT 1")
        print("Database is connected (^_^) : UP")
    except Exception as e:
        print("Oopsie...")
        print("seems like DB is missing or there is some problem in DB connection,see below traceback")
        raise e


async def check_db_disconnected():
    try:
        if not str(SQLALCHEMY_DATABASE_URL).__contains__("sqlite"):
            database = databases.Database(SQLALCHEMY_DATABASE_URL)
            if database.is_connected:
                await database.disconnect()
        print("Database is Disconnected (-_-) : DOWN")
    except Exception as e:
        raise e
