from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.document import document
from routes.query import api
from schemas.document import Document

app = FastAPI()

origins = [
    "http://completoschile.online",
    "https://completoschile.online",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # En producción, define aquí los dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(document)
app.include_router(api)
