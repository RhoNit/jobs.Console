import databases
from configurator.config import get_db_uri

uri = get_db_uri()


async def check_db_connected():
    try:
        if not str(uri).__contains__("sqlite"):
            database = databases.Database(uri)
            if not database.is_connected:
                await database.connect()
                await database.execute("SELECT 1")
        print("Database is connected (^_^) : UP")
        
    except Exception as e:
        print("Seems like DB is missing or there is a problem in connection, see below traceback")
        raise e


async def check_db_disconnected():
    try:
        if not str(uri).__contains__("sqlite"):
            database = databases.Database(uri)
            if database.is_connected:
                await database.disconnect()
        print("Database is disconnected (-_-) : DOWN")
        
    except Exception as e:
        raise e
