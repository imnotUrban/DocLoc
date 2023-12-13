from typing import List
from fastapi import APIRouter
from schemas.document import Document
from controllers.query import query_documents
from pydantic import BaseModel

api = APIRouter()

class QueryOut(BaseModel):
   doc: List[Document]
   count: int

@api.get("/query", response_model=QueryOut)
def filters(all: str = None, from_: str | None = None, to_: str | None = None, cat: str | None = None, page: int | None = 1):
    return query_documents(all, from_, to_, cat, page)