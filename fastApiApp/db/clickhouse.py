import uuid
import datetime
import os
import dotenv
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from clickhouse_sqlalchemy import types, engines


dotenv.load_dotenv()

CH_HOST = os.getenv("CH_HOST")
CH_PORT = os.getenv("CH_PORT")
CH_USER = os.getenv("CH_USER")
CH_PASSWORD = os.getenv("CH_PASSWORD")
CH_DATABASE = os.getenv("CH_DATABASE")

CH_URL = f"clickhouse://{CH_USER}:{CH_PASSWORD}@{CH_HOST}:{CH_PORT}/{CH_DATABASE}"

engine = sqlalchemy.create_engine(CH_URL)

session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = sqlalchemy.orm.declarative_base()


class Record(Base):
    __tablename__ = "records"

    id = sqlalchemy.Column(types.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    text = sqlalchemy.Column(types.String)
    created_at = sqlalchemy.Column(types.DateTime64, default=datetime.datetime.now)

    __table_args__ = (
        engines.MergeTree(order_by=["created_at"]),
        {"comment": "Store records"},
    )
