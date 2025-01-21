import datetime
from typing import List

from pydantic import BaseModel


class RecordRequest(BaseModel):
    text: str


class RecordResponse(BaseModel):
    id: int
    text: str
    created_at: datetime.datetime


class AllRecordsResponse(BaseModel):
    records: List[RecordResponse]
