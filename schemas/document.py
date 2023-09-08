from typing import Optional
from pydantic import BaseModel


class Document(BaseModel):
    id: Optional[int]
    title: str
    text: str
    date: str
    url: str
    state: str
    result: Optional[str]
    lat: Optional[str]
    long: Optional[str]