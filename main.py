from fastapi import FastAPI
from routes.document import document
from routes.geocache import cache
from Rabbit.channelManagement import setupRabbitmq

setupRabbitmq()

app = FastAPI()

app.include_router(document)

#app.include_router(cache, prefix="/cache")