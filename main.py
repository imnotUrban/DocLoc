from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.document import document
from routes.crud import get_all, get_by_date, get_by_category
from schemas.document import Document
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, define aquí los dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(document)

@app.get("/api/news/all/", response_model=list[Document])
def get_news():
   return get_all()

## DD-MM-AAAA
@app.get("/api/news/date/", response_model=list[Document])
def get_news(from_: str, to_= str):
   return get_by_date(from_ = from_, to_ = to_)

# @app.get("/api/news/category/", response_model=list[Document])
# def get_news(categoty: str):
#    return get_by_category(category = categoty)
