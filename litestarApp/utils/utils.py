from db.postgres import session as pg_session
from db.clickhouse import session as ch_session


def get_pg():
    db = pg_session()
    try:
        yield db
    finally:
        db.close()


def get_ch():
    db = ch_session()
    try:
        yield db
    finally:
        db.close()
