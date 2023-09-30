from fastapi import FastAPI
from routes.document import document
from Rabbit.channelManagement import setupRabbitmq

setupRabbitmq()

app = FastAPI()

app.include_router(document)