import datetime
import uuid
from typing import List

from pydantic import BaseModel


class RecordRequest(BaseModel):
    text: str


class RecordResponse(BaseModel):
    id: uuid.UUID
    text: str
    created_at: datetime.datetime


class AllRecordsResponse(BaseModel):
    records: List[RecordResponse]
