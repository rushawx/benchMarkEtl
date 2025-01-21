import uvicorn
from fastapi import FastAPI

from db.postgres import Base as PgBase, engine as pg_engine
from db.clickhouse import Base as ChBase, engine as ch_engine
from handlers.records import router as records_router

app = FastAPI()

app.include_router(records_router)

PgBase.metadata.create_all(bind=pg_engine)
ChBase.metadata.create_all(bind=ch_engine)


@app.get("/")
def root():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
