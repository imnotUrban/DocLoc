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
    lat: str | None = None 
    lng: str | None = None
    
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

    def updateDocLatLng(self, docLat : str, docLng: str):  
        try:
        # Supongamos que tienes una variable self.id que contiene el ID del documento que deseas actualizar
            conn.execute(documents.update().where(documents.c.id == self.id).values(lat=docLat, lng=docLng))
            print("Latitud del documento actualizado correctamente")
            print("Longitud del documento actualizado correctamente")
            conn.commit()
        except Exception as e:
            raise Exception(f"No se ha podido actualizar la Latitud o longitud del documento: {str(e)}")

    def updateSummary(self, summary):
        try:
            conn.execute(documents.update().where(documents.c.id == self.id)).values(summary=summary)
            print("Resumen actualizado")
            conn.commit()
        except Exception as e:
            raise Exception(f"No se ha podido actualizar el resumen: {str(e)}")
        
    def is_title_exists(self) -> bool:
        try:
            result = conn.execute(documents.select().where(documents.c.title == self.title)).fetchone()
            if result is not None:
                print(result)
                document = {"title": result[1], "text": result[2], "date":result[3], "url":result[4], "lat":result[7], "lng":result[8]}
                return document
            else: 
                return None
        except Exception as e:
            raise Exception(f"No se ha podido verificar la existencia del título: {str(e)}")

class Config:
    orm_mode = True