from pydantic import BaseModel
from config.db import conn
from models.geocache import geocache_table

class CacheDocument(BaseModel):
    location_id: int = None
    location: str
    lat: str = None
    lng: str = None
    
    def saveCache(self):
        newDocument = {"location" : self.location, "lat": self.lat, "lng": self.lng}
        print(newDocument)
        conn.execute(geocache_table
                        .insert()
                        .values(newDocument))
        conn.commit()
    
    def print(self):
        print(f"{self.location_id};{self.location};{self.lat};{self.lng}")

class Config:
    orm_mode = True