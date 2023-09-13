from fastapi import FastAPI
from .routes.document import document
from .routes.geocache import cache

app = FastAPI()

app.include_router(document)

app.include_router(cache, prefix="/cache")