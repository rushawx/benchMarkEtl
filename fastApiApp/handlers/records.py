from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.postgres import Record as PgRecord
from db.clickhouse import Record as ChRecord
from models.records import RecordRequest, RecordResponse
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
