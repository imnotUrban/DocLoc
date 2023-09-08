from typing import Optional
from pydantic import BaseModel
from config.db import conn
from models.document import documents


class Document(BaseModel):
    id: Optional[int]
    title: str
    text: str
    date: str
    url: str
    state: int
    result: Optional[str]
    lat: Optional[str]
    long: Optional[str]
    
    def validateField(self):
        ##TODO: Aca debe validar que lo que se ingresó efectivamente es del tipo que se pide, además de ciertas cosas que hay que revisar
        return "xd"
    
    
    #Guarda el documento en la base de datos
    def saveDocin(self):
        newDocument = {"title" : self.title, "text": self.text, "date": self.date, "url":self.url, "state": 0}
        result = conn.execute(documents.insert().values(newDocument))
        conn.commit()
        print("Agregado correctamente")
    
    
    
class Config:
    orm_mode = True