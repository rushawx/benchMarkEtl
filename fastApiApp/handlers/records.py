from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from db.postgres import Record as PgRecord
from db.clickhouse import Record as ChRecord
from models.records import RecordRequest, RecordResponse, AllRecordsResponse
from utils.utils import get_pg, get_ch


router = APIRouter(prefix="/records", tags=["records"])


@router.post("/post_pg")
async def create_record_pg(
    record: RecordRequest, db: Session = Depends(get_pg)
) -> RecordResponse:
    record = PgRecord(text=record.text)
    db.add(record)
    db.commit()
    db.refresh(record)
    return RecordResponse(id=record.id, text=record.text, created_at=record.created_at)


@router.post("/post_ch")
async def create_record_ch(
    record: RecordRequest, db: Session = Depends(get_ch)
) -> RecordResponse:
    record = ChRecord(text=record.text)
    db.add(record)
    db.commit()
    db.refresh(record)
    return RecordResponse(id=record.id, text=record.text, created_at=record.created_at)


@router.get("/get_pg")
async def get_records_pg(db: Session = Depends(get_pg)) -> AllRecordsResponse:
    records = db.query(PgRecord).all()
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


@router.get("/get_ch")
async def get_records_ch(db: Session = Depends(get_ch)) -> AllRecordsResponse:
    records = db.query(ChRecord).all()
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


@router.post("/replicate_pg_to_ch")
async def replicate_pg_to_ch(
    db_pg: Session = Depends(get_pg), db_ch: Session = Depends(get_ch)
):
    records = db_pg.query(PgRecord).all()
    for record in records:
        db_ch.add(ChRecord(text=record.text))
    db_ch.commit()
    return {"message": f"{len(records)} rows replicated successfully!"}


@router.post("/replicate_ch_to_pg")
async def replicate_ch_to_pg(
    db_ch: Session = Depends(get_ch), db_pg: Session = Depends(get_pg)
):
    records = db_ch.query(ChRecord).all()
    for record in records:
        db_pg.add(PgRecord(text=record.text))
    db_pg.commit()
    return {"message": f"{len(records)} rows replicated successfully!"}


@router.delete("/delete_pg")
async def delete_records_pg(db: Session = Depends(get_pg)):
    db.execute(text('TRUNCATE TABLE records;'))
    db.commit()
    return {"message": "All records deleted successfully!"}


@router.delete("/delete_ch")
async def delete_records_ch(db: Session = Depends(get_ch)):
    db.execute(text('TRUNCATE TABLE records;'))
    db.commit()
    return {"message": "All records deleted successfully!"}
