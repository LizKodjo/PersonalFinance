# from contextlib import asynccontextmanager
from fastapi import FastAPI, status
from motor import motor_asyncio
import uvicorn
from config import BaseConfig
from routers.transactions import router as transactions_router

settings = BaseConfig()


# @asynccontextmanager
async def lifespan(app: FastAPI):
    app.client = motor_asyncio.AsyncIOMotorClient(settings.DB_URL)
    app.db = app.client[settings.DB_NAME]
    try:
        app.client.admin.command("ping")
        print("Pinged your deployment.  You have successfully connected to MongoDB")
        print("Mongo address; ", settings.DB_URL)
    except Exception as e:
        print(e)
    yield
    app.client.close()

app = FastAPI(lifespan=lifespan)
app.include_router(transactions_router,
                   prefix="/transactions", tags=["transactions"])


@app.get("/")
async def get_root():
    return {"Message": "Root working"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
