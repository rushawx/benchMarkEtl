from litestar import Router, get, post
from litestar.di import Provide

from sqlalchemy.orm import Session
from sqlalchemy import text

from db.postgres import Record as PgRecord
from db.clickhouse import Record as ChRecord
from models.records import RecordRequest, RecordResponse, AllRecordsResponse
from utils.utils import get_pg, get_ch


@post(path="/post_pg")
async def create_record_pg(
    data: RecordRequest,
    pg_db: Session,
) -> RecordResponse:
    record = PgRecord(text=data.text)
    pg_db.add(record)
    pg_db.commit()
    pg_db.refresh(record)
    return RecordResponse(id=record.id, text=record.text, created_at=record.created_at)


@post("/post_ch")
async def create_record_ch(
    data: RecordRequest,
    ch_db: Session,
) -> RecordResponse:
    record = ChRecord(text=data.text)
    ch_db.add(record)
    ch_db.commit()
    ch_db.refresh(record)
    return RecordResponse(id=record.id, text=record.text, created_at=record.created_at)


@get("/get_pg")
async def get_records_pg(
    pg_db: Session,
) -> AllRecordsResponse:
    records = pg_db.query(PgRecord).all()
    output = []
    for record in records:
        output.append(
            RecordResponse(
                id=record.id,
                text=record.text,
                created_at=record.created_at,
            )
        )
    return AllRecordsResponse(records=output)


@get("/get_ch")
async def get_records_ch(
    ch_db: Session,
) -> AllRecordsResponse:
    records = ch_db.query(PgRecord).all()
    output = []
    for record in records:
        output.append(
            RecordResponse(
                id=record.id,
                text=record.text,
                created_at=record.created_at,
            )
        )
    return AllRecordsResponse(records=output)


@post("/replicate_pg_to_ch")
async def replicate_pg_to_ch(
    pg_db: Session,
    ch_db: Session,
) -> None:
    records = pg_db.query(PgRecord).all()
    for record in records:
        ch_db.add(ChRecord(text=record.text))
    ch_db.commit()
    return {"message": f"{len(records)} rows replicated successfully!"}


@post("/replicate_ch_to_pg")
async def replicate_ch_to_pg(
    pg_db: Session,
    ch_db: Session,
) -> None:
    records = ch_db.query(PgRecord).all()
    for record in records:
        pg_db.add(ChRecord(text=record.text))
    pg_db.commit()
    return {"message": f"{len(records)} rows replicated successfully!"}


@post("/delete_pg")
async def delete_pg(
    pg_db: Session,
) -> None:
    pg_db.execute(text("TRUNCATE TABLE records;"))
    pg_db.commit()
    return {"message": "All records deleted successfully!"}


@post("/delete_ch")
async def delete_ch(
    ch_db: Session,
) -> None:
    ch_db.execute(text("TRUNCATE TABLE records;"))
    ch_db.commit()
    return {"message": "All records deleted successfully!"}


router = Router(
    path="/records",
    route_handlers=[
        create_record_pg,
        create_record_ch,
        get_records_pg,
        get_records_ch,
        replicate_pg_to_ch,
        replicate_ch_to_pg,
        delete_pg,
        delete_ch,
    ],
    dependencies={"pg_db": Provide(get_pg), "ch_db": Provide(get_ch)},
)
