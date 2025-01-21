import uvicorn
from fastapi import FastAPI

from db.postgres import Base, engine
from handlers.records import router as records_router

app = FastAPI()

app.include_router(records_router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
