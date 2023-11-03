from fastapi import FastAPI
from routes.document import document
from routes.query import api
from schemas.document import Document

app = FastAPI()

app.include_router(document)
app.include_router(api)
