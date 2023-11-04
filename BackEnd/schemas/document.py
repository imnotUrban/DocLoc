from pydantic import BaseModel
from sqlalchemy import Date
from datetime import datetime
from config.db import conn
from models.document import documents

class Document(BaseModel):
    id: int | None = None
    title: str
    text: str
    date: str
    category: str
    url: str
    state: int | None = None 
    summary: str | None = None
    location: str | None = None
    lat: str | None = None 
    lng: str | None = None
    
    def saveDocin(self):
        try:
            self.date = datetime.strptime(self.date, "%b %d, %Y @ %H:%M:%S.%f").strftime("%Y-%m-%d")
            newDocument = {"title":self.title, "text":self.text, "date":self.date, "category":self.category, "url":self.url, "state":self.state, "summary": self.summary, "location":self.location, "lat":self.lat, "lng":self.lng}
            result = conn.execute(documents.insert().values(newDocument))
            conn.commit()
            self.id = result.inserted_primary_key[0]
            print("Agregado correctamente")
        except Exception as e:
            raise Exception(f"No se ha podido crear el objeto documento {str(e)}")
    
    def updateDocState(self, docState : int):
        self.state = docState

    def updateDocResult(self, docResult : str):  
        try:
            conn.execute(documents.update().where(documents.c.id == self.id).values(result=docResult))
            conn.commit()
            print("Resultado del documento actualizado correctamente")
        except Exception as e:
            raise Exception(f"No se ha podido actualizar el resultado del documento: {str(e)}")

    def updateSummary(self, summary: str):
        self.summary = summary
        try:
            conn.execute(documents.update().where(documents.c.id == self.id).values(summary=self.summary))
            conn.commit()
            print("Resumen actualizado")
        except Exception as e:
            raise Exception(f"No se ha podido actualizar el resumen: {str(e)}")
        
    def updateDocLocLatLng(self, docLoc: str, docLat : str, docLng: str):  
        self.location = docLoc
        self.lat = docLat
        self.lng = docLng 
        try:
            conn.execute(documents.update().where(documents.c.id == self.id).values(location=self.location, lat=self.lat, lng=self.lng))
            conn.commit()
            print("Documento actualizado correctamente")
        except Exception as e:
            raise Exception(f"No se ha podido actualizar la Latitud o longitud del documento: {str(e)}")
        
    def exists(self) -> bool:
        try:
            result = conn.execute(documents.select().where(documents.c.title == self.title)).fetchone()
            if result is not None:
                return {"title":result[1], "text":result[2], "date":result[3], "category":result[4], "url":result[5], "summary":result[8], "location":result[8], "lat":result[9], "lng":result[10]}
            else: 
                return None
        except Exception as e:
            raise Exception(f"No se ha podido verificar la existencia del título: {str(e)}")

    def geolocalized(self):
        return {"title":self.title, "text":self.text, "date":self.date, "category":self.category, "url":self.url, "summary":self.summary, "location":self.location, "lat":self.lat, "lng":self.lng}

    def __str__(self) -> str:
        return super().__str__()

class Config:
    orm_mode = True