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
    result: str | None = None
    lat: str | None = None 
    long: str | None = None
    
    #Guarda el documento en la base de datos
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
        # Supongamos que tienes una variable self.id que contiene el ID del documento que deseas actualizar
            conn.execute(documents.update().where(documents.c.id == self.id).values(state=docState))
            conn.commit()
            print("Estado actualizado correctamente")
        except Exception as e:
            raise Exception(f"No se ha podido actualizar el estado del documento: {str(e)}")

    def updateDocResult(self, docResult : str):  
        try:
        # Supongamos que tienes una variable self.id que contiene el ID del documento que deseas actualizar
            conn.execute(documents.update().where(documents.c.id == self.id).values(result=docResult))
            conn.commit()
            print("Resultado del documento actualizado correctamente")
        except Exception as e:
            raise Exception(f"No se ha podido actualizar el resultado del documento: {str(e)}")

    def updateDocLatLong(self, docLat : str, docLong: str):  
        try:
        # Supongamos que tienes una variable self.id que contiene el ID del documento que deseas actualizar
            conn.execute(documents.update().where(documents.c.id == self.id).values(lat=docLat))
            conn.commit()
            print("Latitud del documento actualizado correctamente")
            conn.execute(documents.update().where(documents.c.id == self.id).values(long=docLong))
            conn.commit()
            print("Longitud del documento actualizado correctamente")
        except Exception as e:
            raise Exception(f"No se ha podido actualizar la Latitud o longitud del documento: {str(e)}")

    
class Config:
    orm_mode = True