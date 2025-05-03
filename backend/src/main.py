# from contextlib import asynccontextmanager
from fastapi import FastAPI
from motor import motor_asyncio
from config import BaseConfig
from web import user
import uvicorn


# settings = BaseConfig()

# @asynccontextmanager


# async def lifespan(app: FastAPI):
#     app.client = motor_asyncio.AsyncIOMotorClient(settings.DB_URL)
#     app.db = app.client[settings.DB_NAME]

#     try:
#         app.client.admin.command("ping")
#         print("Pinged your deployment.  You have successfully connected to MongoDB!")
#         print("Mongo address: ", settings.DB_URL)
#     except Exception as e:
#         print(e)
#     yield
#     app.client.close()

# app = FastAPI(lifespan=lifespan)

app = FastAPI()
app.include_router(user.router)


@app.get("/")
async def homepage():
    return "This is my homepage"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
