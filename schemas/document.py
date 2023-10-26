from pydantic import BaseModel
from config.db import conn
from models.document import documents

class Document(BaseModel):
    id: int | None = None
    title: str
    text: str
    date: str
    url: str
    state: int | None = None 
    summary: str | None = None
    location: str | None = None
    lat: str | None = None 
    lng: str | None = None
    
    def saveDocin(self):
        try:
            newDocument = {"title" : self.title, "text": self.text, "date": self.date, "url":self.url, "state": 0}
            result = conn.execute(documents.insert().values(newDocument))
            conn.commit()
            self.id = result.inserted_primary_key[0]
            print("Agregado correctamente")
        except Exception:
            raise Exception("No se ha podido crear el objeto documento")
    
    def updateDocState(self, docState : int):
        try:
            conn.execute(documents.update().where(documents.c.id == self.id).values(state=docState))
            conn.commit()
            print("Estado actualizado correctamente")
        except Exception as e:
            raise Exception(f"No se ha podido actualizar el estado del documento: {str(e)}")

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
            print("Resumen actualizado")
            conn.commit()
        except Exception as e:
            raise Exception(f"No se ha podido actualizar el resumen: {str(e)}")
        
    def updateDocLocLatLng(self, docLoc: str, docLat : str, docLng: str):  
        self.location = docLoc
        self.lat = docLat
        self.lng = docLng 
        try:
            conn.execute(documents.update().where(documents.c.id == self.id).values(location=self.location, lat=self.lat, lng=self.lng))
            print("Documento actualizado correctamente")
            conn.commit()
        except Exception as e:
            raise Exception(f"No se ha podido actualizar la Latitud o longitud del documento: {str(e)}")
        
    def exists(self) -> bool:
        try:
            result = conn.execute(documents.select().where(documents.c.title == self.title)).fetchone()
            if result is not None:
                #TODO: Arreglar este return
                document = {"title": result[1], "text": result[2], "date":result[3], "url":result[4], "lat":result[7], "lng":result[8]}
                return document
            else: 
                return None
        except Exception as e:
            raise Exception(f"No se ha podido verificar la existencia del título: {str(e)}")

    def geolocalized(self):
        return {"date": self.date, "summary": self.summary, "location": self.location, "lat": self.lat, "lng": self.lng}

class Config:
    orm_mode = True