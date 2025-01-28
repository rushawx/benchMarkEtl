import uvicorn
from typing import Dict
from litestar import Litestar, Router, get
from handlers.records import router as records_router
from db.postgres import Base as PgBase, engine as pg_engine
from db.clickhouse import Base as ChBase, engine as ch_engine


PgBase.metadata.create_all(bind=pg_engine)
ChBase.metadata.create_all(bind=ch_engine)


@get("/")
def root() -> Dict:
    return {"message": "Hello, World!"}


root_router = Router(
    path="/",
    route_handlers=[root],
)


app = Litestar([root_router, records_router])


if __name__ == "__main__":
    uvicorn.run(app, port=8001)
