from fastapi import FastAPI
from routes.document import document
from routes.crud import get_all, get_by_date, get_by_category
from schemas.document import Document
app = FastAPI()

app.include_router(document)

@app.get("/api/news/all/", response_model=list[Document])
def get_news():
   return get_all()

@app.get("/api/news/date/", response_model=list[Document])
def get_news(from_: str, to_= str):
   return get_by_date(from_ = from_, to_ = to_)

# @app.get("/api/news/category/", response_model=list[Document])
# def get_news(categoty: str):
#    return get_by_category(category = categoty)
