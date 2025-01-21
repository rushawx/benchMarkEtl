from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.postgres import Record
from models.records import RecordRequest, RecordResponse
from utils.utils import get_db


router = APIRouter(prefix="/records", tags=["records"])


@router.post("/")
async def create_record(
    record: RecordRequest, db: Session = Depends(get_db)
) -> RecordResponse:
    record = Record(text=record.text)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record
