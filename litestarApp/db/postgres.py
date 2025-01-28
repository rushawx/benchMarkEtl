import uuid
import datetime
import os

import sqlalchemy
import dotenv
from sqlalchemy.orm import sessionmaker


dotenv.load_dotenv()

PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_DATABASE = os.getenv("PG_DATABASE")

PG_URL = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"

engine = sqlalchemy.create_engine(PG_URL)

session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = sqlalchemy.orm.declarative_base()


class Record(Base):
    __tablename__ = "records"

    id = sqlalchemy.Column(
        sqlalchemy.UUID, primary_key=True, index=True, default=uuid.uuid4
    )
    text = sqlalchemy.Column(sqlalchemy.String)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
