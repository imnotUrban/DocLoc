from fastapi import FastAPI
from routes.document import document

app = FastAPI()

app.include_router(document)